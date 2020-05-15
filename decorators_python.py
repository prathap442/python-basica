'''
  The Decorators are used basically for the sake of the wrapping the functionss in the 
  inside the another function

  - Get the modular functionality in the code
  - To wrap the code with some functionality to be done
'''
import time
import pytest
import pdb

def time_it(func):
   def wrapper(*args,**kwargs):
      start_time = time.time()
      pdb.set_trace()
      totalled_value = func(*args,**kwargs)
      end_time = time.time()
      time_taken = end_time - start_time
      print("the total time taken is {0}-{1} and it is {time_taken}".format(start_time,end_time,time_taken=time_taken)) 
   return wrapper

@time_it
def calculate_square(values):
    total_squared_value = 0
    for value in values:
        total_squared_value += pow(value,2)
    return total_squared_value

def test_calculate_square():
    calculate_square([0,2])


@pytest.fixture(params=[1,2,3])
def factory_bot(passed_value):
    return "the value provided is {passed_value}".format(passed_value= passed_value)

bot_values = factory_bot