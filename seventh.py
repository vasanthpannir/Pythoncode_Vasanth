import pytest
import requests
from requests.auth import HTTPBasicAuth

# Constants for login
URL = "https://10.253.26.242/asc/api/rest/v1/login"
USER = "superadmin"
PW = "Hytrust123!"
HEADERS = {
    "Content-Type": "application/json",
}
TIMEOUT = 10

# Fixture to log in and return the auth token
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

# Example test using the auth token
def test_login(auth_token):
    assert auth_token is not None, "Auth token is None, login failed."

# Test function making a different API request using the auth token
def test_some_api_operation(auth_token):
    url = "https://10.253.26.242/asc/api/v2/guiTransform/resources/protectedResourceHierarchyDetails?v=670293&t=1702395853940&_offset=0&_limit=100&_ordering=name&_counts=true&resourceVendorType=NSXDataCenter"
    headers = {
        "Auth-Token": auth_token,
        "Content-Type": "application/json",
    }
    response = requests.get(url, headers=headers, verify=False)
    assert response.status_code == 200, "API call failed"
    print(f"response header:{response.headers}")
    # Add more assertions based on the expected response structure or content

# # Another test function making another API request using the auth token
# def test_another_api_operation(auth_token):
#     url = ""
#     headers = {
#         "Auth-Token": auth_token,
#         "Content-Type": "application/json",
#     }
#     payload = {"key": "value"}
#     response = requests.post(url, json=payload, headers=headers, verify=False)
#     assert response.status_code == 201, "API call failed"
#     # Add more assertions based on the expected response structure or content

# Optional: Suppress InsecureRequestWarning
@pytest.fixture(autouse=True)
def suppress_insecure_request_warning():
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)