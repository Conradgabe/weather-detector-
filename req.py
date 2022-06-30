import urllib.request
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

# to check the type of error that might occur
def make_request(url):
    try:
        with urlopen(url) as response:
            print(response.status)
            return response.read(), response
    except HTTPError as error:
        print(error.status, error.reason)
    except URLError as error:
        print(error.reason)
    except TimeoutError:
        print("Request timed out")



