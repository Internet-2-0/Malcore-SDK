# Installation

`gcc -o malcore.so -shared -fPIC malcore.c -lcurl`

# Examples

```c
// File upload
ApiRequest execFromUrlRequest = {
  .url = "https://api.malcore.io/api/upload",
  .apiKey = "MYAPIKEY",
  .fileName = "@/path/to/my/file",
  .postData = NULL
}
ApiResponse execFileAnalysisResponse = makeMalcoreApiRequest(&execFromUrlRequest);
// process JSON results

// POST data upload
ApiRequest domainAnalysisRequest = {
  .url = "https://api.malcore.io/api/upload",
  .apiKey = "MYAPIKEY",
  .fileName = NULL,
  .postData = "domain=123.com"
}
ApiResponse domainAnalysisResponse = makeMalcoreApiRequest(&domainAnalysisRequest);
// process JSON results
```