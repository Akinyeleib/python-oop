import random
print(random.randint(12, 34))

from random import randint
print(randint(12, 34))

import programming
print("before: " + str(programming.age))
programming.age = 17
print("after: " + str(programming.age))

programming.greetings_from_new_class("Human")

from programming import greetings_from_new_class

greetings_from_new_class()

# alias
from programming import greetings_from_new_class as greet

greet()

# from student_file import name
# name


