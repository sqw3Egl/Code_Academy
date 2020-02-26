###     Lesson 10 Classes

# 1. TYPES
#     to check the 'type' of a python variable:

print(type(5))

my_dict = {}

print(type(my_dict))

my_list = []

print(type(my_list))

# 2. CLASS
#     A 'class' is a template for a data type, describes the information it will hold
#     to define a class:

class Facade:
  pass                #'pass' keyword is used to stop an Indentation Error, as we have left the class blank.

# 3.INSTANTIATION
#  looks like calling a function. below assigning the class to a variable for use later. NOTICE THE '()'

class Facade:
  pass

facade_1 = Facade()    #this turns the Facade class into an 'object'

#4. OBJECT ORIENTATED PROGRAMMING

# 'type' does the opposite to above and display the class of an object

class Facade:
  pass

facade_1 = Facade()

facade_1_type = type(facade_1)

print(facade_1_type)

#5. CLASS VARIABLES

# a variable that's the same for every instance of the class

#example code:
class Musician:
  title = "Rockstar"

drummer = Musician()
print(drummer.title)       ## syntax for calling the variable is object.variable
# prints "Rockstar"

class Grade:
  minimum_passing = 65

#6. METHODS

# methods are functions that are defined as part of a class
# the first argument of the method function is always 'self'

#example code:
class Dog:
  dog_time_dilation = 7

  def time_explanation(self):
    print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))

pipi_pitbull = Dog()
pipi_pitbull.time_explanation()
# Prints "Dogs experience 7 years for every 1 human year."

class Rules:
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."

#7. METHODS WITH ARGUMENTS

# example code:
class DistanceConverter:
  kms_in_a_mile = 1.609
  def how_many_kms(self, miles):
    return miles * self.kms_in_a_mile

converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)
# prints "8.045"

class Circle:
  pi = 3.14
  def area(self, radius):
    return Circle.pi * (radius ** 2)
  
circle = Circle()

pizza_area = circle.area((12/2))
teaching_table_area = circle.area((36/2))
round_room_area = circle.area((11460/2))  # /2 for the radius

#8. CONSTRUCTORS

# several special methods in python that behave differently from 'normal' methods
#called 'dunder methods' short for double underscore methods. Usually refering to the '__init__' method or CONSTRUCTOR

#example code:

class Shouter:
  def __init__(self):
    print("HELLO?!")

shout1 = Shouter()
# prints "HELLO?!"

shout2 = Shouter()
# prints "HELLO?!"

#passing parameters to the __init__ CONSTRUCTOR:

class Shouter:
  def __init__(self, phrase):
    # make sure phrase is a string
    if type(phrase) == str:

      # then shout it out
      print(phrase.upper())

shout1 = Shouter("shout")
# prints "SHOUT"

shout2 = Shouter("shout")
# prints "SHOUT"

shout3 = Shouter("let it all out")
# prints "LET IT ALL OUT"
#code:
class Circle:
  pi = 3.14
  
  # Add constructor here:
  def __init__(self, diameter):
    print("New circle with diameter: {diameter}".format(diameter=diameter))
    
teaching_table = Circle(36)























