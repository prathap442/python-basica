import pytest
class TestMacMillan:
    def setup_class(self):
      print("Method called before all of the tests being run in the calass")

    def teardown_class(self):
      print("Method called after all of the tests being run in the class") 
 

    def setup_method(self):
      print("Calling setup method before every test case ran in this\n")

    def teardown_method(self):
      print("Calling teardown method after every test case is ran over here\n")

    def test_buzzer(self):
      print("testing the test_buzzer\n")