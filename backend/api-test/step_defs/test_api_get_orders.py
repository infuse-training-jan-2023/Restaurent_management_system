import pytest
from pytest_bdd import scenarios, when, then
import requests

scenarios('../features/get_orders.feature')

order_url = "http://127.0.0.1:8000/orders"

@when('I check order history')
def order_food():
    pytest.api_response = requests.get(order_url)
    print(pytest.api_response)

@then('I should get all the order history')
def check_content_returned():
    data = pytest.api_response.json()
    assert type(data) == list

@then('the api status code should be 200')
def check_status_code():
    assert pytest.api_response.status_code == 200

@then('the api response content type should be json')
def check_content_type():
    assert pytest.api_response.headers['Content-Type'] == 'application/json'
