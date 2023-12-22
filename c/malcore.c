#include "malcore.h"
#include <stdlib.h>

static size_t callBackHandler(void *contents, size_t size, size_t nmemb, void *userp) {
    size_t realsize = size * nmemb;
    HttpResponse *mem = (HttpResponse *)userp;
    mem->data = realloc(mem->data, mem->size + realsize + 1);
    if (mem->data == NULL) {
        return 0;
    }
    memcpy(&(mem->data[mem->size]), contents, realsize);
    mem->size += realsize;
    mem->data[mem->size] = 0;
    return realsize;
}

ApiResponse makeMalcoreApiRequest(const HttpRequestData *request_data) {
    ApiResponse response = {NULL, 0};
    CURL *curl;
    CURLcode res;
    curl_global_init(CURL_GLOBAL_DEFAULT);
    curl = curl_easy_init();

    if(curl) {
        curl_easy_setopt(curl, CURLOPT_URL, request_data->url);
        if (request_data->fileName) {
            curl_easy_setopt(curl, CURLOPT_POSTFIELDS, request_data->fileName);
        } else if (request_data->postData) {
            curl_easy_setopt(curl, CURLOPT_POSTFIELDS, request_data->postData);
        }
        struct curl_slist *headers = NULL;
        char header_string[40];
        sprintf(headerString, "apiKey: %s", request_data->apiKey);
        headers = curl_slist_append(headers, headerString);
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, callBackHandler);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, (void *)&response);
        res = curl_easy_perform(curl);
        curl_easy_cleanup(curl);
        curl_slist_free_all(headers);
        if(res != CURLE_OK) {
            fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
        }
    }
    curl_global_cleanup();
    return response;
}