""" module.py - an example of a Python module """
# create a private variable
__counter = 0

def suml(num_list):
    # use global keyword to modify __counter variable
    global __counter
    # increment __counter variable by 1
    __counter += 1
    # set sum to 0
    the_sum = 0

    for element in num_list:
        # increment the sum by the elements in the list
        the_sum += element
    # return the sum of all the elements in the list
    return the_sum


def prodl(num_list):
    # use global keyword to modify __counter variable
    global __counter    
    # increment __counter by 1
    __counter += 1
    # assign 1 to prod variable
    prod = 1

    for element in num_list:
        prod *= element
    return prod


if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you.")
    my_list = [i+1 for i in range(5)]
    print(suml(num_list) == 15)
    print(prodl(num_list) == 120)

