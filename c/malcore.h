#ifndef MALCORE_H
#define MALCORE_H

#include <curl/curl.h>

typedef struct {
    const char *data;
    size_t size;
} ApiResponse;

typedef struct {
    const char *url;
    const char *apiKey;
    const char *fileName;
    const char *postData;
} ApiRequestData;

ApiResponse makeMalcoreApiRequest(const HttpRequestData *request_data);

#endif
