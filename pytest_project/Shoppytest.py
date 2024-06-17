import pytest
from shopping_cart import ShoppingCart

# initialising the list item

list_item = [{"name": "Banana", "price": 30},
             {"name": "Boost", "price": 130},
             {"name": "Fizz", "price": 30},
             {"name": "Milk", "price": 20},
             {"name": "Bread", "price": 80},
             {"name": "Cheese", "price": 70}]


#Test case 1 check wheather cart is initialsed to 0
@pytest.fixture
def Shop():
    return ShoppingCart(list_item)

# check if cart is initially 0
def test_cartis_initaly_zero(Shop):
    assert Shop.cart=={}

# check adding an item
def test_add_single_item(Shop):
    Shop._addcart("Banana",5)
    assert Shop.cart=={'Banana':5}

# check adding same item update the quantity
def test_add_multiple_item(Shop):
    Shop._addcart("Banana",6)
    Shop._addcart("Banana", 5)
    assert Shop.cart == {'Banana': 11}

# test case to check updation
def test_update_existing_item(Shop):
    Shop._addcart("Banana",6)
    Shop._updatecart("Banana", 2)
    assert Shop.cart == {'Banana': 2}

# test case to check updation of an non exisiting item
def test_update_non_existing_item(Shop):
    Shop._addcart("Banana",6)
    Shop._updatecart("Milk", 2)
    assert Shop.cart == {'Banana': 6}

# test case to check the removal if an existing item
def test_remove_existing_item(Shop):
    Shop._addcart("Banana",6)
    Shop._removecart("Banana")
    assert Shop.cart == {}

# test case to check the removal if an non existing item
def test_remove_non_existing_item(Shop):
    Shop._addcart("Banana",6)
    Shop._removecart("Milk")
    assert Shop.cart == {'Banana': 6}

#Test case for multiplr operation
def test_multiple_operation(Shop):
    Shop._addcart("Banana", 5)
    Shop._addcart("Banana", 5)
    Shop._addcart("Milk", 3)
    Shop._updatecart("Milk", 2)
    Shop._addcart("Fizz", 3)
    Shop._removecart("Milk")
    assert Shop.cart == {'Banana': 10,'Fizz':3}

# Test case for bill print
def test_print_bill(Shop):
    Shop._addcart("Milk", 3)
    Shop._updatecart("Milk", 2)
    Shop._addcart("Fizz", 3)
    assert Shop._printbill() == "Bill Printed"

# Test case for add item with zero quantity
def test_add_item_with_zero_quantity(Shop):
    Shop._addcart("Milk", 0)
    assert Shop._showcart()=={}

# Test case for add item with negative quantity
def test_add_item_with_negative_quantity(Shop):
    Shop._addcart("Milk", -5)
    assert Shop._showcart()=={}

# Test case to update item with zero which delete the item
def test_update_item_with_zero_quantity(Shop):
    Shop._addcart("Milk",5)
    Shop._updatecart("Milk", 0)
    assert Shop._showcart()=={}


