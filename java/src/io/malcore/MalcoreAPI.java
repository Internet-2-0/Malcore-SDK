package io.malcore;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLConnection;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.util.HashMap;
import java.util.Map;
import java.util.Optional;
import java.util.concurrent.CompletableFuture;

public class MalcoreAPI {

    private final String apiKey;
    private static final String BASE_URL = "https://api.malcore.io/api";
    private HttpURLConnection connection;
    private final HashMap<String, Object> parameters = new HashMap<>();
    private MalcoreAction currentAction;
    private final int minimumScansRemaining;
    private boolean ignoreMinimumScansRemaining;

    public MalcoreAPI(String apiKey) {
        this.apiKey = apiKey;
        this.minimumScansRemaining = 10;
        this.ignoreMinimumScansRemaining = false;
    }

    public MalcoreAPI(String apiKey, int minimumScansRemaining) {
        this.apiKey = apiKey;
        this.minimumScansRemaining = minimumScansRemaining;
        this.ignoreMinimumScansRemaining = false;
    }

    public MalcoreAPI prepareRequest(MalcoreAction endpoint) {
        this.currentAction = endpoint;
        return this;
    }

    public MalcoreAPI addParameter(String key, String value) {
        if (this.currentAction.getRequestType().equals("POST")) {
            parameters.put(key, value);
        } else {
            throw new IllegalStateException("Parameters can only be added to POST requests.");
        }
        return this;
    }

    public MalcoreAPI addParameter(String name, File value) {
        try {
            if (value.isFile()) {
                    parameters.put(name, value);
                    return this;
            } else {
                throw new MalcoreException("Invalid file supplied (file not found or is a directory)");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        return this;
    }

    public MalcoreAPI ignoreMinimumScansRemaining() {
        ignoreMinimumScansRemaining = true;
        return this;
    }

    public Optional<String> execute()  {
        try {
            prepareConnection();

            int responseCode = connection.getResponseCode();

            BufferedReader in;
            if (responseCode < HttpURLConnection.HTTP_BAD_REQUEST) {
                in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            } else {
                in = new BufferedReader(new InputStreamReader(connection.getErrorStream()));
            }

            String inputLine;
            StringBuilder response = new StringBuilder();

            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine);
            }
            in.close();

            return Optional.of(response.toString());
        } catch (Exception e) {
            e.printStackTrace();
        }

        return Optional.empty();
    }


    public CompletableFuture<String> executeAsync() {
        return CompletableFuture.supplyAsync(() -> {
            try {
                prepareConnection();
                return getResponse(connection);
            } catch (Exception e) {
                throw new RuntimeException(e);
            }
        });
    }

    private void prepareConnection() throws IOException, MalcoreException {
        if(!ignoreMinimumScansRemaining && getScansRemaining() <= minimumScansRemaining) {
            throw new MalcoreException("Could not execute request, too close to minimum scans. (If you'd like to ignore this, either set the " +
                    "minimum scans to 0 in the constructor or chain the .ignoreMinimumScansRemaining() method)");
        }

        if(getScansRemaining() == 0) {
            throw new MalcoreException("Could not execute request, you have no scans left.");
        }

        URL url = new URL(BASE_URL + currentAction.getEndpoint());

        connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod(currentAction.getRequestType());
        connection.setRequestProperty("apiKey", apiKey);

        if ("POST".equalsIgnoreCase(currentAction.getRequestType())) {
            connection.setDoOutput(true);

            String boundary = Long.toHexString(System.currentTimeMillis());
            connection.setRequestProperty("Content-Type", "multipart/form-data; boundary=" + boundary);

            try (OutputStream outputStream = connection.getOutputStream();
                 PrintWriter writer = new PrintWriter(new OutputStreamWriter(outputStream, StandardCharsets.UTF_8), true)) {

                for (Map.Entry<String, Object> entry : parameters.entrySet()) {
                    if (!(entry.getValue() instanceof File)) {
                        writer.append("--").append(boundary).append("\r\n");
                        writer.append("Content-Disposition: form-data; name=\"").append(entry.getKey()).append("\"\r\n");
                        writer.append("Content-Type: text/plain; charset=UTF-8\r\n\r\n");
                        writer.append(entry.getValue().toString()).append("\r\n");
                        writer.flush();
                    }
                }

                for (Map.Entry<String, Object> entry : parameters.entrySet()) {
                    if (entry.getValue() instanceof File file) {
                        String fileName = file.getName();
                        writer.append("--").append(boundary).append("\r\n");
                        writer.append("Content-Disposition: form-data; name=\"").append(entry.getKey()).append("\"; filename=\"").append(fileName).append("\"\r\n");
                        writer.append("Content-Type: ").append(URLConnection.guessContentTypeFromName(fileName)).append("\r\n\r\n");
                        writer.flush();
                        Files.copy(file.toPath(), outputStream);
                        outputStream.flush(); // Flush to commit the file data
                        writer.append("\r\n");
                        writer.flush(); // Flush to make sure the writer's buffer is written
                    }
                }

                writer.append("--").append(boundary).append("--").append("\r\n");
                writer.flush();
            }
        }
    }

    private String getResponse(HttpURLConnection connection) throws IOException {
        int responseCode = connection.getResponseCode();

        try (BufferedReader in = new BufferedReader(new InputStreamReader(
                responseCode < HttpURLConnection.HTTP_BAD_REQUEST ? connection.getInputStream() : connection.getErrorStream()))) {

            String inputLine;
            StringBuilder response = new StringBuilder();

            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine);
            }

            return response.toString();
        } finally {
            connection.disconnect();
        }
    }

    public int getScansRemaining() {
        try {
            URL url = new URL("https://api.malcore.io/user/scans/available");

            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.setRequestProperty("apiKey", apiKey);

            int responseCode = connection.getResponseCode();
            if (responseCode == HttpURLConnection.HTTP_OK) {
                try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                    String line;
                    StringBuilder response = new StringBuilder();
                    while ((line = reader.readLine()) != null) {
                        response.append(line);
                    }

                    String resp = response.toString();
                    return Integer.parseInt(resp.split("\\{\"scansLeft\":")[1].split(",")[0]);
                }
            } else {
                throw new MalcoreException("Error fetching scans remaining: HTTP error code " + responseCode);
            }
        } catch (IOException | MalcoreException e) {
            e.printStackTrace();
            return -1;
        }
    }



}
