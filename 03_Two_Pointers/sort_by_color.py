#!/usr/bin/env python3

"""
Given an array with n objects colored red, white or blue,
sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: Using library sort function is not allowed.

Example :

Input : [0 1 2 0 1 2]
Modify array so that it becomes : [0 0 1 1 2 2]
"""


class Solution:
    def sortColors(self, a):
        """
        >>> s = Solution()
        >>> s.sortColors([0, 1, 2, 0, 1, 2])
        [0, 0, 1, 1, 2, 2]

        >>> s.sortColors([0, 2, 1])
        [0, 1, 2]

        """
        left, right = 0, len(a) - 1
        i = left

        while i <= right:
            if a[i] == 0:
                a[left], a[i] = 0, a[left]
                left = left + 1
                i = max(i, left)
            elif a[i] == 2:
                a[right], a[i] = 2, a[right]
                right = right - 1
            else:
                i += 1
        return a


if __name__ == '__main__':
    import doctest
    doctest.testmod()
