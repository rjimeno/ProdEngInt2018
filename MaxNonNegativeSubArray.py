#!/usr/bin/env python3

"""
Find out the maximum sub-array of non negative numbers from an array.
The sub-array should be continuous. That is, a sub-array created by choosing
the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the
sub-array. Sub-array A is greater than sub-array B if sum(A) > sum(B).

Example:

A : [1, 2, 5, -7, 2, 3]
The two sub-arrays are [1, 2, 5] [2, 3].
The answer is [1, 2, 5] as its sum is larger than [2, 3]

NOTE: If there is a tie, then compare with segment's length and return segment which has maximum length
NOTE 2: If there is still a tie, then return the segment with minimum starting index
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
