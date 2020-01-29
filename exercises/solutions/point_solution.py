import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.joinpath('point')))

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
    
    def get_coords(self):
        return (self.x, self.y, self.z)

    def __eq__(self, other):
        return self.get_coords() == other.get_coords()
    
    def __str__(self):
        return f'{self.__class__.__name__}(x={self.x}, y={self.y}, z={self.z})'
    
    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Point(self.x * other, self.y * other, self.z * other)
    
    def __rmul__(self, other):
        return self.__mul__(other)

    def __getitem__(self, key):
        return self.get_coords()[key]
    

if __name__ == "__main__":
    doctest.testmod()