import pytest
from pytest_bdd import scenarios, when, then
import requests

scenarios('../features/add_table.feature')

add_table_url = "http://localhost:8000/tables"
booking_details = {
  "user_name": "Jane Doe",
  "table_no": 1,
  "capacity": 2,
  "price": 2000,
  "date": "2020-01-01",
  "slot": "Evening"
}

@when('I book a table')
def display_all_items():
    pytest.api_response = requests.post(add_table_url, json=booking_details)
    print(pytest.api_response)

@then('booking should be added to database')
def check_content_returned():
    data = pytest.api_response.json()
    assert type(data) == dict

@then('api status code should be 200')
def check_status_code():
    assert pytest.api_response.status_code == 200

@then('api response content type should be application/json')
def check_content_type():
    assert pytest.api_response.headers['Content-Type'] == 'application/json'
