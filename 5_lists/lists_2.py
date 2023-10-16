hat = [1, 2, 3, 4, 5]

# ask user to enter a number
user_input = int(input("Please enter a number (integer): \n"))

# replace the middle number in hat list with the user input
hat[2] = user_input

# write a line of code that removes the last element in hat
# using the del instruction

# del hat[-1]
# print(hat)

# using method
hat.pop()
print(hat)



