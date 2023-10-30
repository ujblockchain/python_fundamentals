"""
In programming, there are two main sources of errors:
- Error in the data (incorrect user inputs, corrupted data sources)
- Error in the code (bugs)

In Python, when an error occurs, an exception is raised. An exception is an unexpected event that occurs during the execution of a program.
These errors are syntactically correct
"""
# common exception is a division by zero
# result = 10 / 0 # this will result in a ZeroDivisionError
# print(result)

# print(dir(locals()['__builtins__']))

# we have an access control system that uses age
try:
    # convert user input to integer
    user_age = int(input("Please enter your age: \n"))
    # check if user is allowed on site
    if user_age > 13:
        print("Welcome to our site")
    else:
        print("Not allowed to our site")
except:
	print("Please enter a valid integer")

# catching specific exceptions
try:
    even_numbers = range(2, 20, 2)
    print(even_numbers[8])

except ZeroDivisionError:
    print("Denominator cannot be 0.")

except IndexError:
    print("Index Out of Bound")

# Python try with else clause
"""
The try with else clause is used when we want to run a certain block of code if the try block runs without errors.

"""

try:
    user_age = int(input("Please enter your age: "))
except:
    print("Not an even number!")
else:
    if user_age > 13:
        print("Welcome to our site")
    else:
        print("Not allowed to our site")


# Python try..finally
"""
The finally block is always executed no regardless of if there is an exception or not.
The finally block is optional and there can only be one finally block.
"""
try:
    user_age = int(input("Please enter your age: "))
except:
    print("Not an even number!")
else:
    if user_age > 13:
        print("Welcome to our site")
    else:
        print("Not allowed to our site")
finally:
    print("Thank you for coming.")