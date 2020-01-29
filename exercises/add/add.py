import doctest

def add((matrix1: list, matrix2: list)) -> list:
    """add two matrices elementwise

    Example:
    >>> matrix1 = [[1, -2], [-3, 4]]
    >>> matrix2 = [[2, -1], [0, -1]]
    >>> add(matrix1, matrix2)
    [[3, -3], [-3, 3]]
    """
    pass


if __name__ == "__main__":
    doctest.testmod()