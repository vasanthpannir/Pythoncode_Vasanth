# conftest.py
import pytest
import requests
from requests.auth import HTTPBasicAuth

@pytest.fixture(scope="session")
def auth_token():
    url = "https://10.253.26.242/asc/api/rest/v1/login"
    user = "superadmin"
    pw = "Hytrust123!"
    headers = {
        "Content-Type": "application/json",
    }
    timeout = 10
    response = requests.post(url, verify=False,
                             auth=HTTPBasicAuth(user, pw),
                             headers=headers,
                             timeout=timeout)
    assert response.status_code == 200, "Failed to login"
    auth_token = response.headers.get("Auth-Token")
    assert auth_token is not None, "Authorization token not found"
    return auth_token