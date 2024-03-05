import requests
from requests.auth import HTTPBasicAuth


url = "https://10.253.26.242/asc/api/rest/v1/login"
user = "superadmin"
pw = "Hytrust123!"
headers = {

    "Content-Type": "application/json",
    # Example: "User-Agent": "MyApp/1.0"
}
timeout = 10


def login(url, user, pw, headers, timeout):
    try:

        rsession = requests.post(url, verify=False,
                                 auth=HTTPBasicAuth(user, pw),
                                 headers=headers,
                                 timeout=timeout)


        if rsession.status_code == 200:
            # Extract the Authorization token from the response headers
            auth_token = rsession.headers.get("Auth-Token")

            if auth_token:
                print(f"Login successful! Auth Token: {auth_token}")
                # Further processing can be done here (e.g., parsing response data)
            else:
                print("Authorization token not found in the response headers.")
        else:
            print(f"Login failed with status code: {rsession.status_code}")
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that occur during the request
        print(f"An error occurred: {e}")



login(url, user, pw, headers, timeout)