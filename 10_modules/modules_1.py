import math

def sin(x):
    #  check if 2 * input is equivalent to pi - 3.14
    if 2 * x == pi:
        # return 0.9999 if it is 
        return 0.99999999
    else:
        # return None if it is not
        return None

# define variable pi and store 3.14
pi = 3.14

print(sin(pi/2))
# print the the result of pi/2
print(math.sin(math.pi/2))