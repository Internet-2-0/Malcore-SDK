from msdk.lib.settings import post_data, post_files
from msdk.base.api_schema import Api


class MalcoreApiSdk(Api):

    def __init__(self, api_key, **kwargs):
        super().__init__(api_key, **kwargs)

    def executable_file_analysis(self, filename1):
        url = f"{self.base_url}/upload"
        return post_files(url, filename1=filename1, headers=self.headers, proxies=self.proxy)

    def status_check(self, uuid):
        url = f"{self.base_url}/status"
        return post_data(url, {"uuid": uuid}, proxy=self.proxy, headers=self.headers)

    def pcap_diff(self, filename1, filename2):
        url = f"{self.base_url}/pcapdiff"
        return post_files(url, filename1=filename1, filename2=filename2, headers=self.headers, proxy=self.proxy)

    def packer_checking(self, filename1):
        url = f"{self.base_url}/checkpacked"
        return post_files(url, filename1=filename1, headers=self.headers, proxy=self.proxy)

    def hashsum(self, filename1):
        url = f"{self.base_url}/gethash"
        return post_files(url, filename1=filename1, headers=self.headers, proxy=self.proxy)

    def readable_strings(self, filename1):
        url = f"{self.base_url}/strings"
        return post_files(url, filename1=filename1, headers=self.headers, proxy=self.proxy)

    def import_and_exports(self, filename1):
        url = f"{self.base_url}/impexp"
        return post_files(url, filename1=filename1, headers=self.headers, proxy=self.proxy)

    def deep_static_analysis(self, filename1):
        url = f"{self.base_url}/deepstatic"
        return post_files(url, filename1=filename1, headers=self.headers, proxy=self.proxy)

    def gather_sections(self, filename1):
        url = f"{self.base_url}/sections"
        return post_files(url, filename1=filename1, headers=self.headers, proxy=self.proxy)

    def yara_rule_scanning(self, filename1):
        url = f"{self.base_url}/yara"
        return post_files(url, filename1=filename1, headers=self.headers, proxy=self.proxy)

    def parse_exif_data(self, filename1):
        url = f"{self.base_url}/exif"
        return post_files(url, filename1=filename1, headers=self.headers, proxy=self.proxy)

    def shellcode_emulation(self, shellcode, arch=64):
        url = f"{self.base_url}/shellcode"
        return post_data(url, {"shellcode": shellcode, "arch": arch}, headers=self.headers, proxy=self.proxy)

    def domain_analysis(self, domain):
        url = f"{self.base_url}/domain"
        return post_data(url, {"domain": domain}, headers=self.headers, proxy=self.proxy)

    def android_permission_lookup(self, permission_name):
        url = f"{self.base_url}/androidperms"
        return post_data(url, {"perm": permission_name}, proxy=self.proxy, headers=self.headers)

    def threat_score(self, filename1):
        url = f"{self.base_url}/threatscore"
        return post_files(url, filename1=filename1, headers=self.headers, proxy=self.proxy)

    def ssdeep_comparison(self, ssdeep_hash):
        url = f"{self.base_url}/compare"
        return post_data(url, {"ssdeep_hash": ssdeep_hash}, proxy=self.proxy, headers=self.headers)

    def binary_diffing(self, filename1, filename2):
        url = f"{self.base_url}/bindiff"
        return post_files(url, filename1=filename1, filename2=filename2, headers=self.headers, proxy=self.proxy)

    def script_analysis(self, filename1, script_type):
        url = f"{self.base_url}/scriptanalysis"
        self.headers['Script-Type'] = script_type
        return post_files(url, filename1=filename1, headers=self.headers, proxy=self.proxy)

    def android_manifest_parsing(self, filename1):
        url = f"{self.base_url}/manifest"
        return post_files(url, filename1=filename1, headers=self.headers, proxy=self.proxy)

    def document_file_analysis(self, filename1):
        url = f"{self.base_url}/docfile"
        return post_files(url, filename1=filename1, headers=self.headers, proxy=self.proxy)

    def file_rescanning(self, sha256_id_hash):
        url = f"{self.base_url}/rescan"
        return post_data(url, {"sha256hash": sha256_id_hash})

    def ransom_note_comparison(self, filename1):
        url = f"{self.base_url}/ransomnote"
        return post_files(url, filename1=filename1, headers=self.headers, proxy=self.proxy)

    def execute_from_url(self, url):
        url = f"{self.base_url}/execfromurl"
        return post_data(url, {"url": url}, proxy=self.proxy, headers=self.headers)

    def view_full_asm_hexdump(self, sha256_id, view_type):
        url = f"{self.base_url}/viewfull"
        return post_data(url, {"sha256hash": sha256_id, "view_type": view_type})

    def pcap_analysis(self, filename1):
        url = f"{self.base_url}/pcapanalysis"
        return post_files(url, filename1=filename1, headers=self.headers, proxy=self.proxy)

    def snort_rule_generation(self, filename1):
        url = f"{self.base_url}/snortrule"
        return post_files(url, filename1=filename1, headers=self.headers, proxy=self.proxy)

    def dynamic_analysis(self, filename1):
        url = f"{self.base_url}/dynamicanalysis"
        return post_files(url, filename1=filename1, headers=self.headers, proxy=self.proxy)

    def url_checking(self, url):
        url_ = f"{self.base_url}/urlcheck"
        return post_data(url_, {"url": url}, proxy=self.proxy, headers=self.headers)
