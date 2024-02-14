class Person():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        print(f"Person's name is {self.name}")

    def get_age(self):
        print(f"Person's age is {self.age}")
    
# Inheritance
        # DRY - Don't Repeat Yourself
# base class == super class
# sub- class
class Staff(Person):
    
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    def get_department(self):
        print(f"Person's department is {self.department}")

    def get_age(self):
        print(f"Staff's age is {self.age}")
    


