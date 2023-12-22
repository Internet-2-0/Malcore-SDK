import requests


class UploadError(Exception): pass


class MaintenanceModeActive(Exception): pass


class InvalidApiKeyPassed(Exception): pass


# major.minor.patch.commit
MSDK_VERSION = "0.1.6.8"


def check_invalid_api_key(request_data):
    """
    checks if Forbidden is in the content, if it is that means the wrong API key has been passed
    """
    if request_data.content == b"Forbidden":
        raise InvalidApiKeyPassed(
            "The API key presented got a forbidden result, "
            "is it the correct key? Or do you not have access to this endpoint?"
        )


def check_maintenance_mode(data):
    """
    checks if the server is in maintenance mode from the JSON results
    """
    try:
        if data['isMaintenance']:
            raise MaintenanceModeActive("API is currently in maintenance mode, try again later")
    except:
        return


def check_successful_scan(data):
    """
    checks if the scan was successful or not
    """
    try:
        if not data['success']:
            raise UploadError("Scan was not successful")
    except:
        return


def check_result_type(data):
    """
    checks if there are any error messages in the data output
    """
    errors = []
    try:
        for item in data['data']['messages']:
            try:
                if item['type'] == "danger":
                    errors.append(item['message'])
            except:
                pass
        if len(errors) != 0:
            err_str = ""
            for i, error in enumerate(errors, start=1):
                err_str += f"\n\t#{i} -> '{error}'"
            raise UploadError(f"{len(errors)} total error(s) during upload, error message(s) are as follows: {err_str}")
    except:
        return


def post_files(url, filename1=None, filename2=None, **kwargs):
    """
    POST files to the provided URL can either take 1 file or 2 files
    """
    headers = kwargs.get("headers", None)
    proxy = kwargs.get("proxy", None)

    if proxy is None:
        proxy = {}

    assert headers is not None
    assert type(proxy) == dict
    assert filename1 is not None

    if filename2 is not None:
        file_data = {
           'filename1': open(filename1, "rb"),
           'filename2': open(filename2, "rb")
        }
    else:
        file_data = {
            'filename1': open(filename1, "rb")
        }
    try:
        req = requests.post(url, headers=headers, proxies=proxy, files=file_data)
        check_invalid_api_key(req)
        data = req.json()
        check_result_type(data)
        check_maintenance_mode(data)
        check_successful_scan(data)
        return data['data']
    except Exception as e:
        raise UploadError(f"Got error while POSTing files: {e}")


def post_data(url, data, **kwargs):
    """
    POST data to the provided URL
    """
    proxy = kwargs.get("proxy", None)
    headers = kwargs.get("headers", None)

    assert type(proxy) == dict
    assert headers is not None

    try:
        req = requests.post(url, data=data, headers=headers, proxies=proxy)
        check_invalid_api_key(req)
        data = req.json()
        check_result_type(data)
        check_maintenance_mode(data)
        check_successful_scan(data)
        return data['data']
    except Exception as e:
        raise UploadError(f"Got error POSTing data: {e}")

