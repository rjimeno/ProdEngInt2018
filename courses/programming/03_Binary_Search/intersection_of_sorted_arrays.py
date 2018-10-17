#!/usr/bin/env python3

"""
Find the intersection of two sorted arrays.
OR in other words,
Given 2 sorted arrays, find all the elements which occur in both the arrays.

Example :

Input :
    A : [1 2 3 3 4 5 6]
    B : [3 3 5]

Output : [3 3 5]

Input :
    A : [1 2 3 3 4 5 6]
    B : [3 5]

Output : [3 5]

    NOTE : For the purpose of this problem ( as also conveyed by the sample case ),
    assume that elements that appear more than once in both arrays should be included
    multiple times in the final output.
"""


class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, a, b):
        """
        >>> s = Solution()
        >>> s.intersect([1,2,3,3,4,5,6], [3,3,5])
        [3, 3, 5]

        >>> s.intersect([1,2,3,3,4,5,6], [3,5])
        [3, 5]
        """
        outcome = []
        if 0 < len(a) and 0 < len(b):
            ai, bi = 0, 0
            while ai < len(a) and bi < len(b):
                if a[ai] < b[bi]:
                    ai += 1
                elif b[bi] < a[ai]:
                    bi += 1
                else:  # a[ai] == b[bi]:
                    outcome += [a[ai]]
                    ai += 1
                    bi += 1
        return outcome


if __name__ == '__main__':
    import doctest
    doctest.testmod()
