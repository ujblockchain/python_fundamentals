"""
Python Recursion

Recursion is a technique where a function invokes itself.

Things to remember when dealing with a recursive function

- Base case: final stop point or condition where recursive call needs to stop.
it is used to prevent the occurrence of infinite loops. 

"""
def recursion(count):
    # create the base case
    if count == 500:
        return # exit the function
    else:
        print("Hello, world")
        # increment the count
        recursion(count+1)

# invoke the function 
i = 0 
recursion(i)