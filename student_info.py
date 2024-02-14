num1 = 2
num2 = 3
num3 = num1 + num2

# print('{} + {} = {}'.format())
# Type error on conversion
# print(num1 + ' + ' + num2 + ' = ' + num3) 

# Correct approach
'''
print('1. ' + str(num1) + ' + ' + str(num2) + ' = ' + str(num3)) 
print('2. {} + {} = {}'.format(num1, num2, num3))
print('3. %d + %d = %d' %(num1, num2, num3))
print(f'4. {num1} + {num2} = {num3}')
print(f'5. {num1=} + {num2=} = {num3}')
print(f'6. {num3 + 10 * 2}')
'''
import student_file 

# from student_file import greet  

'''
s1 = student_file.Student()
# s1.greet("fghdk")
# s1.greet()
s1.get_name()
s1.set_name("Boy")
s1.get_name()
s1.set_name("Paul")
s1.get_name()

print("S2")
s2 = student_file.Student()
s2.get_name()

s3 = student_file.Student()
s3.name = "gfhk"
s3. age = 34567
s3.course = "dfghkl"
'''

'''
age = None
print(f"{age=}")
age = 2
print(f"{age=}")
age = "435678"
print(f"{age=}")
age = 2.3
print(f"{age=}")
age = []
print(f"{age=}")
age = ()
print(f"{age=}")
'''

'''
from person import Person
p1 = Person("Pauldtfyguhi", 12)
p1.get_name()
'''

from person import Staff as sf

staff1 = sf("Pauldtfyguhi", 12, "Education")
staff1.get_name()
staff1.get_department()
staff1.get_age()


