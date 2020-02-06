"""mymath - our example math module"""
print("first time import!")

pi = 3.14159  # normally should be a constant, but we want to demonstrate clash with math module


def area(r):
    """area(r): return the area of a circle with radius r."""

    return (pi * r * r)