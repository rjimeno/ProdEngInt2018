#!/usr/bin/env python3

"""
Implement int sqrt(int x).

Compute and return the square root of x.

If x is not a perfect square, return floor(sqrt(x))

Example :

Input : 11
Output : 3

DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY
"""


class Solution:
    # @param m : integer
    # @return an integer
    def sqrt(self, m):
        """
        >>> s = Solution()
        >>> s.sqrt(0)
        0
        >>> s.sqrt(1)
        1
        >>> s.sqrt(2)
        1
        >>> s.sqrt(3)
        1
        >>> s.sqrt(4)
        2
        >>> s.sqrt(5)
        2
        >>> s.sqrt(8)
        2
        >>> s.sqrt(9)
        3
        >>> s.sqrt(10)
        3
        """
        if m < 0:
            m = -m
        if 0 == m or 1 == m:
            return m
        elif 2 == m or 3 == m:
            return 1
        bottom, middle, top = 1, 1, m
        middle_squared = middle * middle
        while bottom < top:
            middle = bottom + ((top - bottom) // 2)
            middle_squared = middle * middle
            if middle_squared < m:
                bottom = middle + 1
            elif middle_squared > m:
                top = middle
            else:
                return middle
        if middle_squared > m:
            middle -= 1
        return middle


if __name__ == '__main__':
    import doctest

    doctest.testmod()
