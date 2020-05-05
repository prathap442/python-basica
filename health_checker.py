# The way we try to work with python modules is to import the modules
# importing can be done as follows
# import random; this is for importing of a random library
# random.randInt(0,45) generates the random integer between 0 and 45

import random # for using radom integer generations
import math # for doing math operations
# modules like numpy and scipy can be used to do extra analysis .
generated_random_int = random.randint(0,45)
print(generated_random_int)
if(generated_random_int > 0):
  print("the generated random int is greater than Zero and is positive")
  print("still in if condition")
  print(math.log10(10)) # this returns 1.0 on screen
elif(generated_random_int < 0):
  print("the generated random int is less than ZEro and is negative")
else:
  print("could not figure out to what kind of number is it")


# What is the value with which the sun is burning in summer season
start = "I am "
age = 20
end = " years old"
output = "{start}{age}{end}".format(start=start,age=age,end=end)
print(output)

# the other way of usng the string interpolatinon is
output = "{0}{1}{2}".format(start,age,end)