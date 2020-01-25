import doctest


# recursiv solution
def deep_flatten(iterable):
    """[summary]
    
    This week we're going to work on flattening iterables. I'd like to you write a function deep_flatten that accepts a list of lists (or lists of tuples and lists) and returns a flattened version of that list of lists.

    Arguments:
        list {[type]} -- a list of lists or tuples

    Examples:
    >>> deep_flatten([[(1, 2), (3, 4)], [(5, 6), (7, 8)]])
    [1, 2, 3, 4, 5, 6, 7, 8]
    >>> deep_flatten([[1, [2, 3]], 4, 5])
    [1, 2, 3, 4, 5]
    """
    flattened = []

    for item in iterable:
        if isinstance(item, (list, tuple)):
            flattened.extend(deep_flatten(item))
        else:
            flattened.append(item)

    return flattened


# iterative solution
def deep_flatten(iterable):
    """Flatten an iterable of iterables."""
    flattened = []
    items = list(iterable)

    while items:
        item = items.pop()

        if isinstance(item, (list, tuple)):
            items.extend(item)
        else:
            flattened.insert(0, item) # because append adds the element at the end

    return flattened


if __name__ == "__main__":
    doctest.testmod()