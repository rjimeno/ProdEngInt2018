#!/usr/bin/env python3

"""
The count-and-say sequence is the sequence of integers beginning as follows:

1, 11, 21, 1211, 111221, ...

1 is read off as one 1 or 11.
11 is read off as two 1s or 21.

21 is read off as one 2, then one 1 or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

Example:

if n = 2,
the sequence is 11.
"""

import re


class Solution:
    """
    #  The countAndSay function below was created by Volker Diels-Grabsch on Aug 18 2013.
    >>> s = Solution()
    >>> s.countAndSay(0)
    1

    >>> s.countAndSay(1)
    1

    >>> s.countAndSay(2)
    '11'

    >>> s.countAndSay(3)
    '21'

    >>> s.countAndSay(4)
    '1211'

    >>> s.countAndSay(5)
    '111221'

    >>> s.countAndSay(6)
    '312211'

    """

    def countAndSay(self, limit, sequence=1):
        if limit > 1:
            return self.countAndSay(limit - 1, "".join(
                [str(len(match.group())) + match.group()[0] for matchNum, match in
                 enumerate(re.finditer(r"(\w)\1*", str(sequence)))]))
        else:
            return sequence


if __name__ == '__main__':
    import doctest
    doctest.testmod()
