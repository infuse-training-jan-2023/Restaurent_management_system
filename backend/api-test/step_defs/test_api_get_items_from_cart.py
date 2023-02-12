import pytest
from pytest_bdd import scenarios, when, then
import requests

scenarios('../features/get_items_from_cart.feature')
user_name = "Jane Doe"
cart_url = f"http://127.0.0.1:8000/cart/{user_name}"


@when('I give the username')
def order_food():
    pytest.api_response = requests.get(cart_url)
    print(pytest.api_response)

@then('I should get all the items in the cart')
def check_content_returned():
    data = pytest.api_response.json()
    assert type(data) == dict

@then('api status code should be 200')
def check_status_code():
    assert pytest.api_response.status_code == 200

@then('api response content type should be application/json')
def check_content_type():
    assert pytest.api_response.headers['Content-Type'] == 'application/json'
