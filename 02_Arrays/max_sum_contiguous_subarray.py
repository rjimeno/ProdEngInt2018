#!/usr/bin/env python3

"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example:

Given the array [-2,1,-3,4,-1,2,1,-5,4],

the contiguous subarray [4,-1,2,1] has the largest sum = 6.

For this problem, return the maximum sum.
"""


class Solution:
    # @param A : tuple of integers
    # @return an integer
    """
    >>> s = Solution()

    >>> A = [1, 2, 5, -7, 2, 3]
    >>> s.maxSubArray(A)
    8

    >>> s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4 ])
    6

    >>> s.maxSubArray([1, 2, 5, -7, 2, 2, 2, 2])
    9

    >>> s.maxSubArray([2, 5, -7, 2, 2, 2, 2])
    8

    >>> s.maxSubArray([-500])
    -500

    >>> s.maxSubArray([-163, -20])
    -20
    """
    # The following function was actually copied from:
    # https://github.com/SKantar/InterviewBit/blob/master/02_Arrays/max_sum_contiguous_subarray.py
    def maxSubArray(self, A):
        tmp_max = tmp_sum = A[0]

        for i in range(1, len(A)):
            tmp_sum = max(A[i], tmp_sum + A[i])
            tmp_max = max(tmp_sum, tmp_max)
        return tmp_max


if __name__ == '__main__':
    import doctest
    doctest.testmod()
