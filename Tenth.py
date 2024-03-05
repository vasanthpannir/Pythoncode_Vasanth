import pytest
import requests
import json
from requests.auth import HTTPBasicAuth


URL = "https://10.253.147.245/asc/api/rest/v1/login"
USER = "superadmin"
PW = "Hytrust123!"
HEADERS = {
    "Content-Type": "application/json",
}
TIMEOUT = 10



@pytest.fixture
def auth_token():
    with requests.post(URL, verify=False,
                       auth=HTTPBasicAuth(USER, PW),
                       headers=HEADERS,
                       timeout=TIMEOUT) as response:
        assert response.status_code == 200, "Login failed with status code: {}".format(response.status_code)
        token = response.headers.get("Auth-Token")
        assert token is not None, "Authorization token not found in the response headers."
        print(f"Auth Token: {token}")  # Print the auth token
        return token



def test_login(auth_token):
    assert auth_token is not None, "Auth token is None, login failed."

def test_some_api_operation(auth_token):
    url = "https://10.253.147.245/asc/api/v2/guiTransform/resources/protectedResourceHierarchyDetails?v=670293&t=1702395853940&_offset=0&_limit=100&_ordering=name&_counts=true&resourceVendorType=NSXDataCenter"
    headers = {
        "Auth-Token": auth_token,
        "Content-Type": "application/json",
    }
    response = requests.get(url, headers=headers, verify=False)
    assert response.status_code == 200, "API call failed"


    response_dict = json.loads(response.text)


    uid_value = response_dict.get('items', [])[0].get('protectedResource', {}).get('uid', None)


    assert uid_value is not None, "UID value not found in the response"


    print("UID Value:", uid_value)


    print("Response Headers:", response.headers)
    print("Response Status Code:", response.status_code)
    print("Response Content (as Dictionary):", response_dict)

def test_inventory_sync(auth_token):

        uid_value = auth_token


        sync_url = f"https://10.253.147.245/asc/api/v2/resources/protectedResources/{uid_value}/refresh"


        headers = {
            "Auth-Token": auth_token,
            "Content-Type": "application/json",
        }

        response = requests.post(sync_url, headers=headers, verify=False)

        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

        assert 'application/json' in response.headers.get('Content-Type', ''), "Unexpected response content type"


        try:
            response_dict = response.json()
        except json.JSONDecodeError as e:

            raise AssertionError(f"Failed to decode response as JSON. Error: {e}")

        assert response_dict.get('status') == 'success', "Inventory sync operation unsuccessful"

        print("Inventory Sync Response Headers:", response.headers)
        print("Inventory Sync Response Status Code:", response.status_code)
        print("Inventory Sync Response Content (as Dictionary):", response_dict)


@pytest.fixture(autouse=True)
def suppress_insecure_request_warning():
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)