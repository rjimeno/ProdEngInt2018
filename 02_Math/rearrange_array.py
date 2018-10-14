#!/usr/bin/env python3

"""
Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.

Example:
Input : [1, 0]
Return : [0, 1]

Lets say N = size of the array. Then, following holds true :
    1. All elements in the array are in the range [0, N-1]
    2. N * N does not overflow for a signed integer
"""

class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference.
    # You do not need to return anything in this case.
    def arrange(self, a):
        """
        >>> s = Solution()

        >>> s.arrange([0])
        [0]

        >>> s.arrange([0, 0])
        [0, 0]

        >>> s.arrange([0, 1])
        [0, 1]

        >>> s.arrange([1, 0])
        [0, 1]

        >>> s.arrange([1, 1])
        [1, 1]

        >>> s.arrange([0, 1, 2])
        [0, 1, 2]

        >>> s.arrange([1, 2, 0])
        [2, 0, 1]

        >>> s.arrange([1, 1, 0])
        [1, 1, 1]

        >>> s.arrange([0, 0, 1])
        [0, 0, 0]

        >>> s.arrange([1, 2, 1])
        [2, 1, 2]

        >>> s.arrange([ 4, 0, 2, 1, 3 ])
        3 4 2 0 1
        """
        # The following solution was copied from:
        # https://github.com/SKantar/InterviewBit/blob/master/02_Math/rearrange_array.py
        n = len(a)
        for i in range(n):
            a[i] += (a[a[i]] % n) * n

        for i in range(n):
            a[i] //= n
        #print(" ".join(str(x) for x in a))

if __name__ == '__main__':
    import doctest
    # doctest.testmod()
    # Will need to use something extra for the tests;
    # perhaps an argument to doctest.testmod() or a decorator.

