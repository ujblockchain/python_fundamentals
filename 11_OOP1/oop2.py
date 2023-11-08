"""
In the previous python script, we set object attributes after their creation.

Python allows us to initialise attributes at the creation of an object. 

the __init__() constructor function is a special function that is called whenever a new object is created (instantiated).

"""

class Employee:
    # constructor function
    def __init__(self, id, name):

        # employee ID
        self.id = id
        # employee name
        self.name = name
    # Instance Variables
    # employee salary
    salary = 0
    # employee experience
    experience = 0

    # create a method - level to determine the employee's level in the company
    def level(self):
        if self.experience > 0 and self.experience < 5:
            print(f"{self.name} is a junior employee")
        elif self.experience > 5:
            print(f"{self.name} is a senior employee.")
        else:
            print(f"{self.name} is a new employee.")
