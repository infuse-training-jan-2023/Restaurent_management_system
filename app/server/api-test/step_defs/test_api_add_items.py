import pytest
from pytest_bdd import scenarios, when, then
import requests

scenarios('../features/add_items.feature')

add_item_url = "http://127.0.0.1:8000/items"

@when('I add new items')
def add_items_to_db():
    pytest.api_response = requests.post(add_item_url)
    print(pytest.api_response)

@then('the items should get saved into database')
def check_content_returned():
    data = pytest.api_response.json()
    assert type(data) == dict

@then('api status code should be 200')
def check_status_code():
    assert pytest.api_response.status_code == 200

@then('api response content type should be application/json')
def check_content_type():
    assert pytest.api_response.headers['Content-Type'] == 'application/json'
