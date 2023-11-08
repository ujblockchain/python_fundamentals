
def factorial_loop(n):
    if n == 0:
        return 1
    result = 1
    for num in range(1,n+1):
        result *=num
    return result


def rec_factorial(n):
    if n == 0:
        return 1
    return n * rec_factorial(n - 1)

# print(factorial_loop(5))
print(rec_factorial(5))