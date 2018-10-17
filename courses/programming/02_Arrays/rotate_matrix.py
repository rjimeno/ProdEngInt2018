#!/usr/bin/env python3

"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

You need to do this in place.

Note that if you end up using an additional array, you will only receive partial score.

Example:

If the array is

[
    [1, 2],
    [3, 4]
]

Then the rotated array becomes:

[
    [3, 1],
    [4, 2]
]
"""
# rjimeno copied this solution from:
# https://github.com/SKantar/InterviewBit/blob/master/02_Arrays/rotate_matrix.py
class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        """
        >>> s = Solution()
        >>> s.rotate([ [ 1, 2 ], [ 3, 4 ] ])
        [[3, 1], [4, 2]]

        >>> s.rotate([ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ])
        [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

        >>> s.rotate([[5, 1, 9,11], [2, 4, 8,10], [13, 3, 6, 7], [15,14,12,16]])
        [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
        """

        n = len(A) - 1

        for i in range(len(A) // 2):
            for j in range(i, n - i):
                t = A[i][j]
                A[i][j] = A[n - j][i]
                A[n - j][i] = A[n - i][n - j]
                A[n - i][n - j] = A[j][n - i]
                A[j][n - i] = t

        return A

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    import doctest
    doctest.testmod()