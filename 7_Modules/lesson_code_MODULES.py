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