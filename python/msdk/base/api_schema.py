import os
import warnings

import msdk.lib.settings as settings


class Api(object):

    """
    schema for the API so we can do class integration
    """

    def __init__(self, api_key, **kwargs):
        extra_headers = kwargs.get("extra_headers", None)
        proxy = kwargs.get("proxy", None)
        is_dev = kwargs.get("is_dev", False)

        if not is_dev:
            self.base_url = "https://api.malcore.io/api"
        else:
            try:
                from dotenv import load_dotenv

                load_dotenv()
                self.base_url = os.getenv("TEST_API_SERVER")
            except ImportError:
                warnings.warn(
                    "no test server configured you either don't have dotenv installed or no .env file was found "
                    "defaulting to live server"
                )
                self.base_url = "https://api.malcore.io/api"

        self.headers = {
            "apiKey": api_key,
            "User-Agent": f"Malcore-SDK/Python {settings.MSDK_VERSION}"
        }
        if proxy is not None:
            assert type(proxy) == str
            self.proxy = {"http": proxy, "https": proxy}
        else:
            self.proxy = {}
        if extra_headers is not None:
            assert type(extra_headers) == dict
            for key in extra_headers.keys():
                if key not in self.headers.keys():
                    self.headers[key] = extra_headers[key]

    def executable_file_analysis(self, filename1):
        pass

    def status_check(self, uuid):
        pass

    def pcap_diff(self, filename1, filename2):
        pass

    def packer_checking(self, filename1):
        pass

    def hashsum(self, filename1):
        pass

    def readable_strings(self, filename1):
        pass

    def import_and_exports(self, filename1):
        pass

    def deep_static_analysis(self, filename1):
        pass

    def gather_sections(self, filename1):
        pass

    def yara_rule_scanning(self, filename1):
        pass

    def parse_exif_data(self, filename1):
        pass

    def shellcode_emulation(self, shellcode, arch=64):
        pass

    def domain_analysis(self, domain):
        pass

    def android_permission_lookup(self, permission_name):
        pass

    def threat_score(self, filename1):
        pass

    def ssdeep_comparison(self, ssdeep_hash):
        pass

    def binary_diffing(self, filename1, filename2):
        pass

    def script_analysis(self, filename1, script_type):
        pass

    def android_manifest_parsing(self, filename1):
        pass

    def document_file_analysis(self, filename1):
        pass

    def file_rescanning(self, sha256_id_hash):
        pass

    def ransom_note_comparison(self, filename1):
        pass

    def execute_from_url(self, url):
        pass

    def view_full_asm_hexdump(self, sha256_id, view_type):
        pass

    def pcap_analysis(self, filename1):
        pass

    def snort_rule_generation(self, filename1):
        pass

    def dynamic_analysis(self, filename1):
        pass

    def url_checking(self, url):
        pass
