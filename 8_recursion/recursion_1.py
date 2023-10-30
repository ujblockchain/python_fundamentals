"""
Function Control of Recursion

"""

def func():
    val = 25
    return val

def test():
    print("UL")

    x = func() #* 2
    y = 15

    result = x + y #+ func()
    return result