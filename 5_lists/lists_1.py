"""
In Python, there are three classes which are sequence types. They are lists, tuple, and range.
These data types are used to hold a collection of items. 

Python lists are the most commonly used and unlike other programs, they
can store items of different data types. 

Python tuples are also an ordered sequence of items however tuples are immutable - once created they cannot be changed
"""
provinces = ["Eastern Cape", "Free State","Gauteng","Kwazulu-Natal", "Limpopo","Mpumalanga", "North West", "Northern Cape", "Western Cape"]

# access items in a list
print(provinces[2]) # print the 3rd item in provinces list

# access the last item using negative index
print(provinces[-1]) # access the last item in provinces

# modify an item in a list

grades = [88, 87, 65 , 70, 60]
# access the item that you want to modify using the index position
grades[4] = 75 # change the last item in the grades from 60 to 75

print(grades)

# instruction on how to delete an item in a list 

del grades[3] # delete the 4th item in the grades list
print(grades)

# attempt to print grades[4]
print(grades[4]) # this will result in an error because we deleted an item - there is no longer 5 items in the list

# add a new item to a grade

grades.append(90) # add 90 to the grades list
print(grades)

# use the insert method
grades.insert(0,90) # 0 is the index position, 90 is the value to insert
print(grades)

# delete an item from a list using pop

deleted_item = grades.pop() # store the item removed from the grades list to variable deleted_item
print(grades) # print the grades list

# use the remove method to delete an item from a list

grades.remove(65)

print(grades)

"""
Extra examples to show you how to work with lists. 
"""

# define a list to store the name of programming languages
languages = ["Python", "Golang", "JavaScript","Java", "C#", "PhP"]

print(languages)

# how to access list items
# access the first item - Python, 2nd item - Golang
print(languages[0]), print(languages[1])

# access the last item , second last item
print(languages[-1], languages[-2])

# modify an item in a list
languages[2] = "Rust"
# print modified list
print(languages)

# delete an item in a list
del languages[4]
# print the number of items in the languages list
print(len(languages))
print(languages)
