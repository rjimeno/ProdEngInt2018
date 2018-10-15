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
    a, b = list(a), list(b)
    while len(a) < len(b):
        a = ['0'] + a
    while len(b) < len(a):
        b = ['0'] + b
    s = ['0'] * len(a)
    #a, b = reversed(a), reversed(b)
    a.reverse()
    b.reverse()
    carry = '0'
    for i in range(len(s)):
        if '0' == a[i]:
            if '0' == b[i]:
                s[i] = carry
                carry = '0'
            elif '1' == b[i]:
                if '0' == carry:
                    s[i] = "1"
                elif '1' == carry:
                    s[i] = '0'
                    carry = "1"
        elif '1' == a[i]:
            if '0' == b[i]:
                if '0' == carry:
                    s[i] = "1"
                elif '1' == carry:
                    s[i] = '0'
            elif '1' == b[i]:
                s[i] = carry
                carry = '1'
    s.reverse()
    if "1" == carry:
        s = ['1'] + s
    return ''.join(s)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
