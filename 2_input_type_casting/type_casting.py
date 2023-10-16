
# input function
user_input = input("Please enter an input..")
# print user_input variable
print(user_input)
# print the data type of user_input variable
print(type(user_input))

# Implicit type casting in Python

# define int value
a = 15
# print the type of variable a
print(type(a))

# define variable b to store float value
b = 12.0

# print the type of variable b
print(type(b))

# implicit type casting
c = a * b # this operation will turn c into a float
print(type(c))

# Explicit type casting 
# float(), int(), str()

# redefine a and set it to 5
a = 5 

# typecast a to float
a_float = float(a)
print(type(a_float))

# float string
float_str = "12.0"
float_value = float(float_str)
print(type(float_value))


# int() function
# convert string to int
b = "12"
b_int = int(b)
print(type(b_int))

# str() function
# convert int to a string 

b_int = 15 # redefine to 15
# convert b_int to string
b_str = str(b_int)
# print the type of variable b_str
print(type(b_str))

# convert string to a float
a = "5.2"
# print the type of the result of the float function with input variable a
print(type(float(a)))


