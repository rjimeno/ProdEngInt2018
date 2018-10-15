#!/usr/bin/env python3

"""
Given two binary strings, return their sum (also a binary string).

Example:

a = "100"

b = "11"

Return a + b = “111”.
"""

class Solution:
    def addBinary(self, a, b):
        return add_binary_strings(a, b)

def add_binary_strings(a, b):
    """
    >>> add_binary_strings("0", "0")
    '0'

    >>> add_binary_strings("0", "1")
    '1'

    >>> add_binary_strings("1", "0")
    '1'

    >>> add_binary_strings("1", "1")
    '10'

    >>> add_binary_strings("0", "10")
    '10'

    >>> add_binary_strings("1", "10")
    '11'

    >>> add_binary_strings("0", "11")
    '11'

    >>> add_binary_strings("1", "11")
    '100'
    """
    a, b = int(a, 2), int(b, 2)
    s = "{:b}".format(a + b)
    return s


if __name__ == '__main__':
    import doctest
    doctest.testmod()
