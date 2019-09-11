#!/usr/bin/env python3

class Solution:
    # https://www.interviewbit.com/problems/min-steps-in-infinite-grid/
    def coverPoints(self, A, B):
        """
        >>> s = Solution()
        >>> A = [ 4, 8, -7, -5, -13, 9, -7, 8 ]
        >>> B = [ 4, -15, -10, -3, -13, 12, 8, -8 ]
        >>> s.coverPoints(A, B)
        108
        >>> A = [ 13, -12, 10, 11, -7, 13,  4, 14, -2,  12, -3,  8, 13, -2, 10,  6,  0, -1,  7, -13,   4, -4, -10, -7,  3, 5,  9, -5, 3 ]
        >>> B = [  0,   0, 14,  0, 12, -8, -2, -8,  1, -11,  8, 10,  9, 10, -9, -6, -1, -2, 11,   8, -11, 12,  -1,  5, -8, 0, -5,  7, 0 ]
        >>> s.coverPoints(A, B)
        370
        """
        if len(A) != len(B) or 0 == len(A):
            steps = None
        else:
            steps = 0
            c_x, c_y = A[0], B[0]
            for i in range(1, len(A)):
                d_x, d_y = A[i], B[i]
                steps_x, steps_y = abs(d_x - c_x), abs(d_y - c_y)
                steps += max(steps_x, steps_y)
                c_x, c_y = d_x, d_y
        return steps

if __name__ == '__main__':
    import doctest
    doctest.testmod()
