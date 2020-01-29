import doctest

class Point:
    """
    custom class for points

    :Examples:
    >>> p1 = Point(1, 2, 3)
    >>> str(p1)
    'Point(x=1, y=2, z=3)'
    >>> p2 = Point(1, 2, 3)
    >>> p1 == p2
    True
    >>> p2.x = 4
    >>> p1 == p2
    False
    >>> str(p2)
    'Point(x=4, y=2, z=3)'
    >>> p1 = Point(1, 2, 3)
    >>> p2 = Point(4, 5, 6)
    >>> p1 + p2
    Point(x=5, y=7, z=9)
    >>> p3 = p2 - p1
    >>> p3
    Point(x=3, y=3, z=3)
    >>> p1 = Point(1, 2, 3)
    >>> p2 = p1 * 2
    >>> p2
    Point(x=2, y=4, z=6)
    >>> p1 = Point(1, 2, 3)
    >>> x, y, z = p1
    >>> (x, y, z)
    (1, 2, 3)
    """
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    

if __name__ == "__main__":
    doctest.testmod()