"""
An object is an entity that has attributes and behaviours.

attributes - name, age, colour
behaviour - running, jumping, eating

A class is a blueprint for that object


"""

class Dog:
    # class attributes
    name = ""  # empty string
    age = 0

class Employee:
    # define attribute
    # employee ID
    id = 0
    # employee name
    name = ""
    # employee salary
    salary = 0
    # employee experience
    experience = 0

    def level(self):
        if self.experience > 0 and self.experience < 5:
            print(f"{self.name} is a junior employee")
        elif self.experience > 5:
            print(f"{self.name} is a senior employee.")
        else:
            print(f"{self.name} is a new employee.")




# create a dog object
dog1 = Dog()  # created a dog1 object
print(type(dog1))  # class Dog

# give dog1 a name
dog1.name = "Lucky"
# give dog1 an age
dog1.age = 1  # years

# create another dog object
dog2 = Dog()
print(type(dog2))  # class Dog

# give dog2 a name
dog2.name = "Spotty"
# give dog1 an age
dog2.age = 2 # years

# access attributes
print(f"{dog1.name} is {dog1.age} years old!")
print(f"{dog2.name} is {dog2.age} years old!")

# create an employee object

employee1 = Employee()
employee2 = Employee()

# access and define values for object attributes

employee1.id = 1111
employee1.name = "Thabo Johnson"
employee1.salary = 21212

employee2.id = 1000
employee2.name = "Jessica Timothy"
employee2.salary = 51215