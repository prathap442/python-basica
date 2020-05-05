class Coin:
  def __init__(self, rareColour="Marrow", **kwargs):
    # a very crucial part here is that the inheritance possessed class from Coin class being parent
    # can be done by setting the new instance methods using 
    # setattr(self, key, value)
    for (key,value) in kwargs.items():
      setattr(self,key,value)

    self.rare = self.rarest_value
    self.thickness = self.coin_thickness
    self.num_of_edges = 1
    self.heads = self.coin_heads
    self.colour = self.coin_colour
  
  def rust(self):
    self.colour = self.rusty_colour

  def clean(self):
    self.colour = self.clean_colour

  def __del__(self):
    print('Coin is spent')


# inheritance from Coin to Pound can be achieved by
# class OnePound(<ParentClass>):
class OnePound(Coin):
  def __init__(self):
    data = {
      "rusty_colour": "brown",
      "clean_colour": "clean_pound_gold_color",
      "coin_heads": True,
      "coin_thickness": 1.32,
      "rarest_value": "Ethirium",
      "coin_colour": "brown"
    }
    #using the property of the inheritance
    super().__init__("sfsjk",**data)

  def pound_method(self):
    print('this is the method dedicated to the pound only')

class TwoPound(Coin):
  def __init__(self):
    data = {
      "rusty_colour": "two_pound_rusty",
      "clean_colour": "two_pound_clean",
      "coin_heads": True,
      "coin_thickness": 1.23,
      "rarest_value": "Plutonium",
      "coin_colour": "Two_pound_coin_colour"
    }
    #using the property of the inheritance
    super().__init__("sfsjk",**data)

  def pound_method(self):
    print('this is the method dedicated to the pound only')

class ThreePound(Coin):
  def __init__(self):
    data = {
      "rusty_colour": "three_pound_rusty",
      "clean_colour": "three_pound_clean",
      "coin_heads": True,
      "coin_thickness": 1.23,
      "rarest_value": "Plutonium",
      "coin_colour": "three_pound_coin_colour"
    }
    #using the property of the inheritance
    super().__init__("sfsjk",**data)

  def pound_method(self):
    print('this is the method dedicated to the pound only')


class FourPound(Coin):
  def __init__(self):
    data = {
      "rusty_colour": "four_pound_rusty",
      "clean_colour": "four_pound_clean",
      "coin_heads": True,
      "coin_thickness": 1.23,
      "rarest_value": "Plutonium",
      "coin_colour": "four_pound_coin_colour"
    }
    #using the property of the inheritance
    super().__init__("sfsjk",**data)

  def pound_method(self):
    print('this is the method dedicated to the pound only')

coins = [OnePound(),TwoPound(),ThreePound()]
for coin in coins:
  attributes = [coin.coin_colour, coin.coin_thickness]
  print("the coin has the following attributest colour:{}- thickness{}".format(coin.coin_colour,coin.coin_thickness))


'''
  What is Polymorphism?
  polymorphism


Generally, the ability to appear in many forms. 
In object-oriented programming, polymorphism refers to a programming language's ability to 
process objects differently depending on their data type or class. 
More specifically, 
  it is the ability to redefine methods for derived classes. 
For example, given a base class shape, 
   polymorphism enables the programmer to define different area methods for any number of derived classes, such as circles, rectangles and triangles. No matter what shape an object is, applying the area method to it will return the correct results.
Polymorphism is considered to be a requirement of any true object-oriented programming language (OOPL).
'''
