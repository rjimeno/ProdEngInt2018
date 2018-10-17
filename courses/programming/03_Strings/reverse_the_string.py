#!/usr/bin/env python3

"""
Given an input string, reverse the string word by word.

Example:

Given s = "the sky is blue",

return "blue is sky the".

        1. A sequence of non-space characters constitutes a word.
        2. Your reversed string should not contain leading or trailing
            spaces, even if it is present in the input string.
        3. If there are multiple spaces between words, reduce
            them to a single space in the reversed string.
"""


class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, p):
        """
        >>> s = Solution()
        >>> s.reverseWords("the sky is blue")
        'blue is sky the'
        """
        sp = p.split()
        rsp = reversed(sp)
        srsp = ' '.join(rsp)
        return srsp


if __name__ == '__main__':
    import doctest
    doctest.testmod()
