import pytest
from pytest_bdd import scenarios, when, then
import requests

scenarios('../features/delete_item.feature')
user_name = "Jane Doe"
item_name = "samosa"
cart_url = f"http://127.0.0.1:8000/cart/{user_name}/{item_name}"


@when('I give the username and item name')
def delete_item_in_cart():
    pytest.api_response = requests.delete(cart_url)
    print(pytest.api_response)

@then('the item should get deleted from the cart')
def check_content_returned():
    data = pytest.api_response.json()
    assert type(data) == dict

@then('api status code should be 200')
def check_status_code():
    assert pytest.api_response.status_code == 200

@then('api response content type should be application/json')
def check_content_type():
    assert pytest.api_response.headers['Content-Type'] == 'application/json'

user_name = "anis"
item_name = "samosa"
cart_url1 = f"http://127.0.0.1:8000/cart/{user_name}/{item_name}"

@when('I give the username and item name which is not there in cart')
def delete_invalid_item_in_cart():
    pytest.api_response = requests.delete(cart_url1)
    print(pytest.api_response)

@then('api status code should be 200')
def check_status_code():
    assert pytest.api_response.status_code == 200

@then('api response content type should be application/json')
def check_content_type():
    assert pytest.api_response.headers['Content-Type'] == 'application/json'


@when('I give the username and item name and change method')
def delete_invalid_item_in_cart():
    pytest.api_response = requests.put(cart_url1)
    print(pytest.api_response)

@then('api status code should be 405')
def check_status_code():
    assert pytest.api_response.status_code == 405

@then('api response content type should be application/json')
def check_content_type():
    assert pytest.api_response.headers['Content-Type'] == 'application/json'
