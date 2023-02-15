import pytest
from pytest_bdd import scenarios, when, then
import requests

scenarios('../features/checkout.feature')
user_name = "Jane Doe"
checkout_url = f"http://127.0.0.1:8000/checkout/{user_name}"


@when('I click on checkout')
def checkout_items():
    pytest.api_response = requests.delete(checkout_url)
    print(pytest.api_response)

@then('the items get saved into orders history')
def check_content_returned():
    data = pytest.api_response.json()
    assert type(data) == dict

@then('api status code should be 200')
def check_status_code():
    assert pytest.api_response.status_code == 200

@then('api response content type should be application/json')
def check_content_type():
    assert pytest.api_response.headers['Content-Type'] == 'application/json'
