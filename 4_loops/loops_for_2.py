"""calculate the sum of numbers from 1 to 100"""
# initialise sum of sequence to zero
total = 0
for num in range(1, 101):
    # increment the total variable by the num in sequence
    total += num # total = total + num
    print(f"running total - {total} - num: {num}")

"""Calculate the sum of the even numbers from 1 to 200"""
total = 0

for num in range(2,201,2):
    # increment the total variable by the num in sequence
    total += num # total = total + num
    print(f"running total - {total} - num: {num}")
