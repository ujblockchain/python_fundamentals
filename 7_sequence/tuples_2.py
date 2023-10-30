"""
Access elements in a tuple.
Just like lists, tuples can be accessed using
1 - Indexing
2 - Negative indexing
3 - Slicing

Remember - 
During the slicing operation, the start index is inclusive but the end index is exclusive.
"""

# indexing  
# access a tuple elements with indexing
languages = ("English", "isiXhosa", "isiZulu","Sesotho", "Xitsonga", "Afrikaans")
print(languages[2]) # print the third element - isiZulu
print(languages[0]) # print the first element - English

# Negative indexing

print(languages[-1]) # print the last element - Afrikaans
print(languages[-4]) # print the 4th element from the right - isiZulu

# Slicing
# remember, slicing is used to access a range of items by using the colon operator
print(languages[0:3]) # print (English, isiXhosa, isiZulu)

# slicing a tuple will return - A TUPLE!
print(type(languages[0:3]))

# print elements to the 3
print(languages[:-3])

print(languages[:]) # print all items in the languages tuple