#!/usr/bin/env python3

"""
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, a, b):
        """
        >>> s = Solution()
        >>> s.diffPossible(b=4, a=[1, 3, 5])
        1
        """
        for i in range(len(a) - 1):
            for j in range(i + 1, len(a)):
                if a[j] - a[i] < b:
                    continue
                elif a[j] - a[i] == b:
                    return 1
                else:
                    break
        return 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()
