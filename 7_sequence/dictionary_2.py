# accessing items in a dictionary
# create a dictionary
country_capitals = {
    "South Africa": "Pretoria",
    "Egypt": "Cairo",
    "Kenya": "Nairobi"
}

# Access dictionary items 
""" The value of a dictionary item can be accessed by placing the key inside square brackets."""
print(country_capitals["Egypt"]) # Cairo

print(country_capitals["Kenya"]) # Nairobi

# get method can also be used to access dictionary items
print(country_capitals.get("Kenya")) # Nairobi

# Python dictionaries are mutable

# Change dictionary items
country_capitals["South Africa"] = "Cape Town" 
print(country_capitals)

# add items to a dictionary
"""A new item can be added to a dictionary by assigning a value to a new key that doesn't exist in the dictionary."""
country_capitals["Namibia"] = "Windhoek"
print(country_capitals)

# remove items
del country_capitals["Namibia"]

# pop method 
removed_capital = country_capitals.pop("South Africa") # cape town

# checking if a key is in a dictionary
print("South Africa" in country_capitals) # False

# iterating through dictionary
# create a dictionary
country_capitals = {
    "South Africa": "Pretoria",
    "Egypt": "Cairo",
    "Kenya": "Nairobi"
}

# print the dictionary keys one by one
for country in country_capitals:
    print(country)

print("-"* 50)

# print the dictionary values one by one
for country in country_capitals:
    capital = country_capitals[country]
    print(capital)

print("-"* 50)

# print the dictionary values one by one
for capital in country_capitals.values():
    print(capital)

