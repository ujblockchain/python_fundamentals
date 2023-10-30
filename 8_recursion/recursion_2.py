"""
Python Recursion

Recursion is a technique where a function invokes itself.

Things to remember when dealing with a recursive function

- Base case: final stop point or condition where recursive call needs to stop.
it is used to prevent the occurrence of infinite loops. 


Advantages of recursion

1 - Used to create clean and elegant code
2 - Complex tasks can be broken down and simplified using recursion
3 - Sequence generation is simpler with recursion compared to nested iteration

Disadvantages of recursion
1 - Logic behind recursion can be hard to follow
2 - Recursive calls are expensive and take up a lot of memory and time
3 - Recursive functions can be difficult to debug
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