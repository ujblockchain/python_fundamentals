"""
Methods with tuples

Tuples are immutable, there are no methods that add items or remove items from a tuple

"""

my_tuple = ("P","Y","T","H","O","N")

# count the number of items in a tuple
print(len(my_tuple))

# concatenation of a tuple
my_tuple_concat = my_tuple + my_tuple
print(my_tuple_concat)

my_tuple2 = my_tuple * 2
print(my_tuple2)

print(my_tuple2 == my_tuple_concat)

# count the number of occurrences of an element in a tuple
p_count = my_tuple.count("P") # case sensitive
print(p_count)

# iterating through a tuple
languages = ("English", "isiXhosa", "isiZulu","Sesotho", "Xitsonga", "Afrikaans")
for language in languages:
    print(languages)

# check if an item exits in a tuple
print("French" in languages) # False
print("isiXhosa" in languages) # True