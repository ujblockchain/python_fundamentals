# operand1 boolean operator operand2

a = 5
b = 25
print(a != b)  # True

"""
Create a program that takes a parameter x as input (int) and print True if the value is greater than or equal to 100,
and False if the value is less than 100
"""
# greet the user 
print("Good day .. let's play a game \n")
# collect user input 
user_input = input("Enter a number... \n ")

# convert the user_input to int
user_input_int = int(user_input)

if user_input_int >= 100:
    print(True)
else:
    print(False)

# store the result of the comparison 
# is 1 equal to 5?
c = (1==5) # False

#conditionals with strings - remember case matters
print("John" == "john")
print("Tsepho" == "tsepho")
print("Tsepho" != "tsepho")
print("John" != "Tshepho")
