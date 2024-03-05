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

# Optional: Suppress InsecureRequestWarning
@pytest.fixture(autouse=True)
def suppress_insecure_request_warning():
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)