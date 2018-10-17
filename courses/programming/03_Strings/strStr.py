#!/usr/bin/env python3

"""
Please Note:

Another question which belongs to the category of questions which are intentionally stated vaguely.
Expectation is that you will ask for correct clarification or you will state your assumptions before you start coding.

Implement strStr().

    strstr - locate a substring ( needle ) in a string ( haystack ).

Try not to use standard library string functions for this question.

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

    NOTE:

    Good clarification questions:

        What should be the return value if the needle is empty?

        What if both haystack and needle are empty?

    For the purpose of this problem, assume that the return value should be -1 in both cases.
"""

class Solution:
    # @param needle : string
    # @param haystack : string
    # @return an integer
    def strStr(self, haystack, needle):
        """
        >>> s = Solution()
        >>> s.strStr("a", "a")
        0

        >>> s.strStr("ab", "b")
        1

        >>> s.strStr("ab", "a")
        0

        >>> s.strStr("abc", "bc")
        1

        >>> s.strStr("bc", "abc")
        -1

        >>> s.strStr("abc", "")
        0

        >>> s.strStr("", "abc")
        -1

        """
        if len(haystack) < len(needle):
            outcome = -1
        elif 0 == len(needle):
            outcome = 0
        else:
            for i in range(len(haystack) - (len(needle) - 1)):
                if haystack[i] == needle[0]:
                    for offset in range(1, len(needle)):
                        if haystack[i + offset] == needle[offset]:
                            continue
                        else:
                            break
                    else:
                        outcome = i
                        break
            else:
                outcome = -1
        return outcome

if __name__ == '__main__':
    import doctest
    doctest.testmod()
