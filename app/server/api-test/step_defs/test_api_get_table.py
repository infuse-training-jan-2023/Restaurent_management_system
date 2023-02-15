import pytest
from pytest_bdd import scenarios, when, then
import requests

scenarios('../features/get_all_tables.feature')

add_item_url = "http://127.0.0.1:8000/tables"

@when('I fetch the tables')
def display_all_items():
    pytest.api_response = requests.get(add_item_url)
    print(pytest.api_response)

@then('all the booking tables are displayed')
def check_content_returned():
    data = pytest.api_response.json()
    assert type(data) == dict

@then('api status code should be 200')
def check_status_code():
    assert pytest.api_response.status_code == 200

@then('api response content type should be application/json')
def check_content_type():
    assert pytest.api_response.headers['Content-Type'] == 'application/json'
