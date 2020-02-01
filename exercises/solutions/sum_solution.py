import doctest


def mysum(*numbers):
    """The challenge here is to write a mysum function that does the same thing as the built-in sum function. However, instead of taking a single sequence as a parameter, it should take a variable number of arguments. Thus while we might invoke sum([1,2,3]), we would instead invoke mysum(1,2,3) or mysum(10,20,30,40,50).

    Examples:
    >>> mysum(1,2,3)
    6
    >>> mysum(-1,0,1)
    0
    >>> mysum(10,20,30,40,50)
    150
    >>> mysum(*[1,2,3,4,5])
    15
    """
    output = 0
    for number in numbers:
            output += number

    return output

if __name__ == "__main__":
    doctest.testmod()