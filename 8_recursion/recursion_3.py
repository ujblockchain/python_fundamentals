"""Recursion tracing tree"""


def rec(n):
    if n == 0:
        return
    print(n)
    rec(n - 1)


def rec2(n):
    # base condition
    if n == 0:
        return
    rec2(n - 1)
    print(n)


def rec3(n):
    # base condition
    if n == 0:
        return
    print(f"UL - {n}")
    rec3(n - 1)
    print(f"UL - {n}")

rec3(3)
