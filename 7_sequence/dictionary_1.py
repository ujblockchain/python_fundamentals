"""
A dictionary is a collection that stores data in key-value pairs.

They are created by KEY:VALUE pairs inside curly brackets {}, separated by commas.

# The keys must be immutable, such as tuples, strings, integers. Mutable objects like lists cannot be used as keys.

"""

# create a dictionary
country_capitals = {
    "South Africa": "Pretoria",
    "Egypt": "Cairo",
    "Kenya": "Nairobi"
}
# print the dictionary
print(country_capitals)


# immutable keys - valid dictionary
ex_dict = {
    1: "Hello world!",
    (1,2): "Monday, Tuesday",
    3: ["Today", "October", 2023]
}

inv_dict = {
    1: "Hello",
    [1,2]: "Monday" # TypeError
}

# get the size of a dictionary
print(len(country_capitals))