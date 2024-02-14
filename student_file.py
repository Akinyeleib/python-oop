class Student():

    # constructor: initialises members
    def __init__(self):
        self.name = None
        self.age = None
        self.course = None


    def greet(self, name="Overwrite"):
        print("Hello from student " + str(self.age))

    def set_name(self, new_name):
        print(f"name changed from {self.name} to {new_name}")
        self.name = new_name

    def get_name(self):
        print(f"Student's name is {self.name}")


