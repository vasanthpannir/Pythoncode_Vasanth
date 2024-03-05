import requests
# Replace with your actual URL, payload data, and certificate path
url = 'https://10.253.26.251/asc/api/rest/v1/login'
payload = {'username': 'superadmin', 'password': 'Hytrust123!'}
certificate_path = ('C:/Users/pannirv/Downloads/tomcatcert.pem', 'r')

# Send POST request with a custom certificate
response = requests.post(url, data=payload, verify=certificate_path)
print(response.text)

# Check the response
# if response.status_code == 200:
#     print("POST request was successful!")
#     print("Response content:")
#     print(response.text)
#
#     # You can also extract headers, cookies, etc., if needed
#     auth_token = response.headers.get('Authorization')
#     if auth_token:
#         print(f"Auth Token: {auth_token}")
# else:
#     print(f"POST request failed with status code {response.status_code}")
#     print("Response content:")
#     print(response.text)