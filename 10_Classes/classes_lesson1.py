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

# 9. INSTANCE VARIABLES

#example code:
class FakeDict:
  pass

fake_dict1 = FakeDict()
fake_dict2 = FakeDict()

fake_dict1.fake_key = "This works!"
fake_dict2.fake_key = "This too!"

# Let's join the two strings together!
working_string = "{} {}".format(fake_dict1.fake_key, fake_dict2.fake_key)
print(working_string)
# prints "This works! This too!"

#my code:
class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

# 10. ATTRIBUTE FUNCTIONS

# example code:
class NoCustomAttributes:
  pass

attributeless = NoCustomAttributes()

try:
  attributeless.fake_attribute
except AttributeError:
  print("This text gets printed!")

# prints "This text gets printed!"

hasattr(attributeless, "fake_attribute")
# returns False

getattr(attributeless, "other_fake_attribute", 800)
# returns 800, the default value

#my code:
how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in how_many_s:
  if hasattr(element, "count"):
    print(element.count("s"))

# 11. SELF

# example code
class SearchEngineEntry:
  def __init__(self, url):
    self.url = url

codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")

print(codecademy.url)
# prints "www.codecademy.com"

print(wikipedia.url)
# prints "www.wikipedia.org"

class SearchEngineEntry:
  secure_prefix = "https://"
  def __init__(self, url):
    self.url = url

  def secure(self):
    return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)

codecademy = SearchEngineEntry("www.codecademy.com")

print(codecademy.secure())
# prints "https://www.codecademy.com"

print(wikipedia.secure())
# prints "https://www.wikipedia.org"

# my code:
class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    
    self.radius = diameter / 2
    
  def circumference(self):
    return 2 * self.pi * self.radius
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

#12. EVERYTHING IS AN OBJECT

# example code:

class FakeDict:
  pass

fake_dict = FakeDict()
fake_dict.attribute = "Cool"

dir(fake_dict)
# Prints ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attribute']

That’s certainly a lot more attributes than we defined! Python automatically adds a number of attributes to all objects that get created. These internal attributes are usually indicated by double-underscores. But sure enough, attribute is in that list.

Do you remember being able to use type() on Python’s native data types? This is because they are also objects in Python. Their classes are int, float, str, list, and dict. These Python classes have special syntax for their instantiation, 1, 1.0, "hello", [], and {} specifically. But these instances are still full-blown objects to Python.

fun_list = [10, "string", {'abc': True}]

type(fun_list)
# Prints <class 'list'>

dir(fun_list)
# Prints ['__add__', '__class__', [...], 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

Above we define a new list. We check it’s type and see that’s an instantiation of class list. We use dir() to explore its attributes, and it gives us a large number of internal Python dunder attributes, but, afterward, we get the usual list methods.

# my code:

print(dir(5))

def this_function_is_an_object():
  return "woo"
  
print(dir(this_function_is_an_object))
  
#13. STRING REPRESENTATION

class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius
  
  def __repr__(self):
    return "Circle with radius " "{radius}".format(radius=self.radius)
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza, teaching_table, round_room)

#14. REVIEW

class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)      

class Grade:
  minimum_passing = 65
  
  def __init__(self, score):
    self.score = score
    
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))






















