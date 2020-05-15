import pytest
from checkout import Checkout
import pdb

@pytest.fixture
def checkout():
  c1 = Checkout()
  return c1

# should be abled to create the checkout instance
def test_add_items_to_dashboard(checkout):
    '''check if the dashboard of the checkout class can add items'''
    checkout.add_items_to_board("item1",2,45)
    assert('item1' in checkout.dashboard.keys())

def test_can_change_item_quantity(checkout):
    '''to check if the quantity gets updated for the item '''    
    checkout.add_items_to_board("item1",2,45)
    assert('item1' in checkout.dashboard.keys())
    current_quantity = (checkout.dashboard['item1']['quantity'])
    new_additional_quantity = 32
    expected_quantity = checkout.dashboard['item1']['quantity'] + new_additional_quantity
    checkout.add_quantity("item1",32)
    assert(checkout.dashboard_item_quantity("item1") == 36)

def test_check_raise_error_improper_quantity(checkout):
    with pytest.raises(Exception):
      checkout.add_items_to_board('items1','a')
      

def add_one_more_item_to_checkout_dashboard(checkout):
    '''to test if the dashboard can accumulate multiple items'''
    checkout.add_items_to_board('items2',4,35)

def test_check_item_in_board_negative(checkout):
    '''to test if the item in the dashboard can be negative'''
    checkout.add_items_to_board('items2',-90)
    assert(checkout.dashboard['items2']['quantity'] == 0 )