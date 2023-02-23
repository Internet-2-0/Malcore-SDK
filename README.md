# Malcore SDK

This package is a software development package for the Malcore API. It provides the functionality to import Malcore into your project and use the API to perform analysis.

# How to use

Usage is simple, in order to use the API simply import the SDK, in order to use the utilities simply import the utilities:

```python
# import the API library
from msdk.api import MalcoreApiSdk
# optional import the utility library
from msdk.utils.file_utils import is_windows_pe_file


# enable your API key you get from https://malcore.io
api = MalcoreApiSdk("MY-API-KEY")
# whatever file you want to use
filename = "/path/to/my/file.exe"
# check if the file is the correct kind
if is_windows_pe_file(filename):
    results = api.threat_score(filename)
    # process results
else:
    # process other
```

This will allow you to use multiple endpoints from Malcore that you have access to via your API key. It also allows you to implement endpoints into the API if you have access to certain endpoints. For example, implementing an endpoint to search:

```python
# import the API schema
from msdk.base.api_schema import Api
# import the POST request function
from msdk.lib.settings import post_data


# create my own API class with the API schema as the object
class MyApi(Api):
    
    def __init__(self, api_key, **kwargs):
        super().__init__(api_key, **kwargs)
    
    # implement the new search function
    def search(self, sha256hash):
        pass


# implement the search function into a new class using the MyAPI class as the object
class ImplementNewEndpoint(MyApi):
    
    def __init__(self, api_key, **kwargs):
        super().__init__(api_key, **kwargs)
    
    # make the request from the search function
    def search(self, sha256hash):
        url = f"{self.base_url}/search"
        return post_data(url, {"sha256hash": sha256hash}, headers=self.headers, proxy=self.proxy)


# add my API key
api = ImplementNewEndpoint("MY-API-KEY")
results = api.search("1234")
# process results
```

This allows users the ability to add endpoints to the SDK as they become available to them.


# Installation

Malcore SDK requires Python 3.8+ to use installation is simple run `pip install msdk` optionally you can manually install by running:

```bash
git clone https://github.com/internet-2-0/Malcore-SDK
cd Malcore-SDK
python setup.py install
```