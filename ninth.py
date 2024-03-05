import pytest
import requests
import json

# Constants
BASE_URL = "https://10.253.26.242"
LOGIN_URL = f"{BASE_URL}/asc/api/rest/v1/login"
RESOURCE_URL = f"{BASE_URL}/asc/api/v2/guiTransform/resources/protectedResourceHierarchyDetails"
USER = "superadmin"
PW = "Hytrust123!"
HEADERS = {"Content-Type": "application/json"}
VERIFY_SSL = False  # Should be True in production

# Suppress InsecureRequestWarning
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

@pytest.fixture(scope="session")
def auth_token():
    """Fixture to log in and retrieve the authentication token."""
    response = requests.post(LOGIN_URL, verify=VERIFY_SSL, auth=(USER, PW), headers=HEADERS)
    assert response.status_code == 200, f"Login failed with status code: {response.status_code}"
    token = response.headers.get("Auth-Token")
    assert token, "Auth token not found"
    return token

@pytest.fixture(scope="session")
def resource_uid(auth_token):
    """Fixture to access a resource using the auth token and extract the UID."""
    headers = {**HEADERS, "Auth-Token": auth_token}
    params = {"v": "670293", "t": "1702395853940", "_offset": 0, "_limit": 100, "_ordering": "name", "_counts": "true", "resourceVendorType": "NSXDataCenter"}
    response = requests.get(RESOURCE_URL, headers=headers, params=params, verify=VERIFY_SSL)
    assert response.status_code == 200, "Failed to access resource"
    data = response.json()
    uid = data.get('items', [])[0].get('protectedResource', {}).get('uid')
    assert uid, "UID not found"
    return uid

def test_inventory_sync(auth_token, resource_uid):
    """Test to perform an inventory sync with the extracted UID."""
    sync_url = f"{BASE_URL}/asc/api/v2/resources/protectedResources/{resource_uid}/refresh"
    headers = {**HEADERS, "Auth-Token": auth_token}
    response = requests.post(sync_url, headers=headers, verify=VERIFY_SSL)
    # Assuming the successful sync operation returns a 200 or 202 status code
    assert response.status_code in [200, 202], f"Inventory sync failed with status code: {response.status_code}"