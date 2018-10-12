#!/usr/bin/env python3

"""
Given a sorted array of integers, find the number of occurrences of a given target value.
Your algorithm’s runtime complexity must be in the order of O(log n).
If the target is not found in the array, return 0

**Example : **
Given [5, 7, 7, 8, 8, 10] and target value 8,
return 2.
"""

FIND_FIRST = True
FIND_LAST = False


class Solution:

    def findCount(self, a, x):
        """
        >>> s = Solution()
        >>> s.findCount(x=8, a=[5, 7, 7, 8, 8, 10])
        2

        >>> s.findCount(x=5, a=[5, 7, 7, 8, 8, 10])
        1

        >>> s.findCount(x=9, a=[5, 7, 7, 8, 8, 10])
        0

        #>>> s.findCount(x=9, a=[5, 7, 7, 8, 8, 10])
        #-1

        >>> s.findCount(x=10, a=[5, 7, 7, 8, 8, 10])
        1
        """
        first = binary_search(a, x, FIND_FIRST)
        if first < 0:
            return 0  # One (wrong) way to indicate x was not found.
        last = binary_search(a, x, FIND_LAST)
        return last - first + 1


def binary_search(a, x, find):
    """
    >>> binary_search(find=FIND_FIRST, x=8, a=[5, 7, 7, 8, 8, 10])
    3
    >>> binary_search(find=FIND_LAST, x=8, a=[5, 7, 7, 8, 8, 10])
    4

    >>> binary_search(find=FIND_FIRST, x=5, a=[5, 7, 7, 8, 8, 10])
    0
    >>> binary_search(find=FIND_LAST, x=5, a=[5, 7, 7, 8, 8, 10])
    0

    >>> binary_search(find=FIND_FIRST, x=10, a=[5, 7, 7, 8, 8, 10])
    5
    >>> binary_search(find=FIND_LAST, x=10, a=[5, 7, 7, 8, 8, 10])
    5

    >>> binary_search(find=FIND_FIRST, x=9, a=[5, 7, 7, 8, 8, 10])
    -2
    >>> binary_search(find=FIND_LAST, x=9, a=[5, 7, 7, 8, 8, 10])
    -4

    """
    low = 0
    high = len(a) - 1
    result = -4 if not find else -2  # Trick to return useful nonsense if not found.
    while low <= high:
        mid = (low + high) // 2
        if x == a[mid]:
            result = mid
            if FIND_FIRST == find:
                high = mid - 1
            else:  # Then find last (FIND_LAST) instead.
                low = mid + 1
        elif x < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return result


if __name__ == '__main__':
    import doctest

    doctest.testmod()
