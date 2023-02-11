import pytest
from pytest_bdd import scenarios, when, then
import requests

scenarios('../features/insert_order.feature')

order_url = "http://127.0.0.1:8000/orders"
order_data = {
  "items": [
    "string"
  ],
  "price": 0,
  "status": "prep",
  "date": "2023-02-09 11:36:10.260068"
}


@when('I order a food')
def order_food():
    pytest.api_response = requests.post(order_url, json=order_data)
    print(pytest.api_response)

@then('order should get placed')
def check_content_returned():
    data = pytest.api_response.json()
    assert type(data) == dict

@then('the api status code should be 200')
def check_status_code():
    assert pytest.api_response.status_code == 200

@then('the api response content type should be json')
def check_content_type():
    assert pytest.api_response.headers['Content-Type'] == 'application/json'
