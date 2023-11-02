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