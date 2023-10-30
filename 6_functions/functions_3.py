def access_control(student=True):
    # greet the person
    print("Good day!")
    if not student: # this is a negation statement
        # if person is not student
        # exit the function
        return
    # if the person is a student
    # welcome them to Blockchain 101!
    print("Welcome to Blockchain 101!")

"""
not True -> False
not False -> True

"""

# calculate force function
def calculate_force(mass, acc=9.81):
    return mass * acc

# calculate your weight using calculate_force function
my_weight = calculate_force(99)
print(f"My weight is {my_weight}N!")
