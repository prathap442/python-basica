import pdb
from math import pi
class Circle:
  def __init__(self,r):
    self.radius = r
    if(r <= 0):
      myError = ValueError('a should be a positive')
      raise myError
    self.area = pi*(r**2)
  def area(self):
    self.area