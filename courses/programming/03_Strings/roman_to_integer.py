#!/usr/bin/env python3

"""
Given an integer, convert it to a roman numeral, and return a string
corresponding to its roman numeral version

Input is guaranteed to be within the range from 1 to 3999.

Example :

Input : 5
Return : "V"

Input : 14
Return : "XIV"

    Note : This question has a lot of scope of clarification from the interviewer.
    Please take a moment to think of all the needed clarifications and see the
    expected response using “See Expected Output”

    For the purpose of this question, https://projecteuler.net/about=roman_numerals
    has very detailed explanations.
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
    def romanToInt(self, roman):
        """
        >>> s = Solution()
        >>> s.romanToInt("XX")
        20

        >>> s.romanToInt("XIV")
        14
        """
        total = 0
        for c, v in RESOLVER:
            while roman.startswith(c):
                total += v
                roman = roman[len(c):]
        return total

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


if __name__ == '__main__':
    import doctest
    doctest.testmod()
