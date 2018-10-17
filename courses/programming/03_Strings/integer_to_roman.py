#!/usr/bin/env python3

"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

Read more details about roman numerals at Roman Numeric System

Example :

Input : "XIV"
Return : 14

Input : "XX"
Output : 20
"""


RESOLVER = [
    ('M', 1000),
    ('CM', 900),
    ('D', 500),
    ('CD', 400),
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1)
]


class Solution:
    # @param A : string
    # @return an integer
    def intToRoman(self, value):
        """
        >>> s = Solution()
        >>> s.intToRoman(20)
        'XX'

        >>> s.intToRoman(14)
        'XIV'
        """
        ans = ''

        for rom, ara in RESOLVER:
            cnt = value // ara
            ans += rom * cnt
            value -= cnt * ara
            if not value:
                break
        return ans