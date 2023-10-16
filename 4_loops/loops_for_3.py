"""Iterating over strings"""

random_string = "Iterate over strings"
count = 0
for char in random_string:
    # check if character is a vowel
    if char in "aeiouAEIOU":
        # if it is a vowel

        # print the following
        print(f"{char} is a vowel")
        # increment the count by 1
        count += 1 # count = count + 1

print(count)