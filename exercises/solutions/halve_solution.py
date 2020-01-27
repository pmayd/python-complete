from typing import List, Tuple, Any
import doctest


def halve(list_of_things: List[Any]) -> Tuple[List[Any], List[Any]]:
    """Take a list and return the first and second half.
    
    Arguments:
        list_of_things {List[Any]} -- list to cut in half
    
    Returns:
        Tuple[List[Any], List[Any]] -- a tuple with first and second half

    Examples:
    >>> halve([1, 2, 3, 4])
    ([1, 2], [3, 4])
    >>> halve([[1, 2], "hi", 1, {4}])
    ([[1, 2], 'hi'], [1, {4}])
    >>> halve([1,2,3])
    ([1], [2, 3])
    """
    N = len(list_of_things)
    return list_of_things[:N//2], list_of_things[N//2:]


if __name__ == "__main__":
    doctest.testmod()
