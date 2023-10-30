"""
A tuple is similar to a list
- tuples are immutable while lists are mutable
- tuples and lists can store different types
"""

# create an empty tuple
empty_tuple = ()
print(empty_tuple)

# create a tuple having integers
integer_tuples = (1, 2, 3, 4, 5)
print(integer_tuples)

# create a tuple with a mixture of integers and tuples
mix_tuples = (1, 2.0, 3, 4, 5.0, 6.6)
print(mix_tuples)

# create a tuple with a mixture of datatypes
mix_tuples_2 = (1, "Hello world", 3.5, ["Hello",2.9, 5, ("2",3)])
print(mix_tuples_2)


# create a tuple with one element
tup1 = ("test") # not a tuple
tup2 = ("test",) # a tuple

print(f"{tup1} is a {type(tup1)}")
print(f"{tup2} is a {type(tup2)}")

