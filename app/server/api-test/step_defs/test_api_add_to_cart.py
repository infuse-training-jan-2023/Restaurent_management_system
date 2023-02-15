import pytest
from pytest_bdd import scenarios, when, then
import requests

scenarios('../features/add_to_cart.feature')

cart_url = "http://127.0.0.1:8000/cart"
cart_data = {
  "user_name": "Jane Doe",
  "items": [
    {
      "item_name": "vodapav",
      "quantity": 1,
      "price": 10
    }
  ]
}

@when('I add items to cart')
def order_food():
    pytest.api_response = requests.post(cart_url, json=cart_data)
    print(pytest.api_response)

@then('items should be added to cart')
def check_content_returned():
    data = pytest.api_response.json()
    assert type(data) == dict

@then('api status code should be 200')
def check_status_code():
    assert pytest.api_response.status_code == 200

@then('api response content type should be application/json')
def check_content_type():
    assert pytest.api_response.headers['Content-Type'] == 'application/json'
