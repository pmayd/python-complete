import doctest


def deep_flatten(iterable):
    """[summary]
    
    This week we're going to work on flattening iterables. I'd like to you write a function deep_flatten that accepts a list of lists (or lists of tuples and lists) and returns a flattened version of that list of lists.

    Arguments:
        iterable {[type]} -- a list of lists or tuples

    Examples:
    >>> deep_flatten([[(1, 2), (3, 4)], [(5, 6), (7, 8)]])
    [1, 2, 3, 4, 5, 6, 7, 8]
    >>> deep_flatten([[1, [2, 3]], 4, 5])
    [1, 2, 3, 4, 5]
    """
    pass


if __name__ == "__main__":
    doctest.testmod()