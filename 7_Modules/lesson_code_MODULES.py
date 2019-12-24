# Import datetime from datetime below:

from datetime import datetime

current_time = datetime.now()
print(current_time)
print(dir(datetime))

##############################

# Import random below:
import random

# Create random_list below:
random_list = [random.randint(1,101) for i in range(101)]

# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)

###################################

#Plots a graph using random numbers and pyplot modules. 
NOTE: random.sample() must have range() or [1, 2, 3, 4, 5] list to work.


import codecademylib3_seaborn
from matplotlib import pyplot as plt
import random

# Add your code below:

numbers_a = range(1, 13)
numbers_b = random.sample(range(1000), 12)

plt.plot(numbers_a, numbers_b)
plt.show()

###################################################



# Import Decimal below:
from decimal import Decimal

# Fix the floating point math below:
two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)

####################################################
#library.py

# Add your always_three() function below:
def always_three(num):
  return 3


#script.py

# Import library below:

from library import always_three

# Call your function below:

print(always_three())

############################################

Modules: Python
Modules Python Review

You’ve learned:

    what modules are and how they can be useful
    how to use a few of the most commonly used Python libraries
    what namespaces are and how to avoid polluting your local namespace
    how scope works for files in Python

Programmers can do great things if they are not forced to constantly 
reinvent tools that have already been built. With the power of modules, 
we can import any code that someone else has shared publicly.

In this lesson, we covered some of the Python Standard Library, 
but you can explore all the modules that come packaged with every 
installation of Python at the Python Standard Library documentation.

This is just the beginning. Using a package manager (like conda or pip3), 
you can install any modules available on the Python Package Index.

The sky’s the limit!
