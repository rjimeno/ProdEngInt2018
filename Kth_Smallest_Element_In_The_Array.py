#!/usr/bin/env python3

"""
Kth Smallest Element in the Array

Find the kth smallest element in an unsorted array of non-negative integers.

Definition of kth smallest element

    kth smallest element is the minimum possible n such that there are at least k elements in the array <= n.
    In other words, if the array A was sorted, then A[k - 1] ( k is 1 based, while the arrays are 0 based )

NOTE
You are not allowed to modify the array ( The array is read only ).
Try to do it using constant extra space.

Example:

A : [2 1 4 3 2]
k : 3

answer : 2
"""


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, a, b):
        """
        >>> s = Solution()
        >>> s.kthsmallest(b=3, a=[ 74, 90, 85, 58, 69, 77, 90, 85, 18, 36 ])
        58

        >>> s.kthsmallest(b=1, a=[ 74, 90, 85, 58, 69, 77, 90, 85, 18, 36 ])
        18

        >>> s.kthsmallest(b=3, a=[2, 1, 4, 3, 2])
        2
        """
        smalls = [float("inf")] * b
        for n in a:
            for i in range(len(smalls)):
                if n < smalls[i]:
                    smalls.insert(i, n)
                    smalls.pop()
                    break
        return smalls.pop()
