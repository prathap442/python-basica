import random
class Coin:
  #constructor
  def __init__(self,rare = False): 
    if rare:
      self.value =  1.25
    else:
      self.value = 1.00
    self.colour =  'orange' 
    self.num_edges =  1
    self.diameter = 0.24
    self.thickness = 1.3
    self.heads = True
  
  def flip(self):
    random_values = [True,False]
    self.heads = random.choice(random_values)
 
  def rust(self):
    self.colour = "brownish"

  def clean(self):
    self.colour = "orange"

  def __del__(self): #destruction method
    print("Coin has been spent!!")

#To load the file into the python shell we first go into the python shell using 
'''
  >>> execfile('coins.py') #this is used to load the coins.py script
  >>> coin1 = Coin()
'''
