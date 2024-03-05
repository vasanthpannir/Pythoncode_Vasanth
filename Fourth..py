import pytest
from Third import login

@pytest.fixture
def authenticated_session():

    url = "https://10.253.26.242/asc/api/rest/v1/login"
    user = "superadmin"
    pw = "Hytrust123!"
    headers = {"Content-Type": "application/json"}
    timeout = 10


    login(url, user, pw, headers, timeout)

    # Return the session object or any data needed for your tests
    return {'url': url, 'user': user, 'password': pw, 'headers': headers}


def test_example(authenticated_session):

    url = authenticated_session['url']
    user = authenticated_session['user']
    password = authenticated_session['password']
    headers = authenticated_session['headers']


    assert len(user) > 0
    assert len(password) > 0
    assert 'Content-Type' in headers
