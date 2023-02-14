import pytest
from pytest_bdd import scenarios, when, then
import requests

scenarios('../features/add_table.feature')

add_table_url = "http://127.0.0.1:8000/tables"
table = {
      "table_no": 5,
        "capicity": 8,
        "date": "-",
        "from_time": "-",
        "to_time": "-",
        "available": True,
        "price": 15000
}
@when('I add a table')
def add_table():
    pytest.api_response = requests.post(add_table_url,json=table)
    print(pytest.api_response)

@then('table should be added')
def check_table_returned():
    data = pytest.api_response.json()
    print(data)
    assert type(data) == dict

@then('api status code should be 200')
def check_api_status():
    assert pytest.api_response.status_code == 200

@then('api response content type should be application/json')
def check_api_content_type():
    assert pytest.api_response.headers['content-Type'] == 'application/json'
