package io.malcore;

public enum MalcoreAction {

        PCAP_DIFF("/pcapdiff", "POST"),
        PCAP_ANALYSIS("/pcapanalysis", "POST"),
        PACKER_CHECKING("/checkpacked", "POST"),
        DEEP_STATIC_ANALYSIS("/deepstatic", "POST"),
        GATHER_SECTIONS("/sections", "POST"),
        SHELLCODE("/shellcode", "POST"),
        BINARY_DIFF("/bindiff", "POST"),
        SCRIPT_ANALYSIS("/scriptanalysis", "POST"),
        RANSOM_NOTE_COMPARISON("/ransomnote", "POST"),
        SNORT_RULE_GENERATION("/snortrule", "POST"),
        HASH_CHECKSUM("/gethash", "POST"),
        STRINGS("/strings", "POST"),
        IMPORTS_AND_EXPORTS("/impexp", "POST"),
        STATUS("/status", "POST"),
        YARA_RULE_SCAN("/yara", "POST"),
        PARSE_EXIF_DATA("/exif", "POST"),
        DOMAIN_ANALYSIS("/domain", "POST"),
        THREAT_SCORE("/threatscore", "POST"),
        SSDEEP_COMPARISON("/compare", "POST"),
        EXECUTE_FROM_URL("/execfromurl", "POST"),
        EXECUTABLE_FILE_ANALYSIS("/upload", "POST"),
        DOCUMENT_FILE_ANALYSIS("/docfile", "POST"),
        URL_CHECKING("/urlcheck", "POST"),
        BROWSER_EXTENSION_ANALYSIS("/browserext", "POST"),
        ANDROID_PERMISSIONS_LOOKUP("/androidperms", "POST"),
        ANDROID_MANIFEST_PARSE("/manifest", "POST"),
        PHONE_APPLICATION_ANALYSIS("/phoneapp", "POST"),
        DYNAMIC_ANALYSIS("/dynamicanalysis", "POST");

        private final String endpoint;
        private final String requestType;

        MalcoreAction(String endpoint, String requestType) {
            this.endpoint = endpoint;
            this.requestType = requestType;
        }

        public String getEndpoint() {
            return endpoint;
        }

        public String getRequestType() {
            return requestType;
        }
    }