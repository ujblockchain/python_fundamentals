# generating lists using range function
# range generates a sequence from 0:
# range(4) - 0 , 1 , 2 , 3
# list() - a built in function that turns a sequence data type to a list
my_list = list(range(4))
print(my_list)

# generate a list with for loop and range function
my_list = [] # create an empty list

for i in range(5):
    # we use the insert method which is specific to the list data type
    my_list.insert(0, i)
# this will create a reversed sequence of range(5)
# range(5) - 0, 1, 2, 3, 4

print(my_list) # 4, 3, 2, 1, 0

