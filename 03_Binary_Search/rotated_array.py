#!/usr/bin/env python3

"""
Suppose a sorted array A is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array will not contain duplicates.

        NOTE 1: Also think about the case when there are duplicates. Does your current solution work? How does the time complexity change?*

PROBLEM APPROACH:

Note: If you know the number of times the array is rotated, then this problem becomes trivial. If the number of rotation is x, then minimum element is A[x].
Lets look at how we can calculate the number of times the array is rotated.
"""


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, a):
        """
        >>> s = Solution()
        >>> a = [15, 22, 23, 28, 31, 38, 5, 6, 8, 10, 12]
        >>> s.findMin(a)
        5

        >>> a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        >>> s.findMin(a)
        1
        """
        i = find_rotation_count(a)
        if -1 == i:
            return -1  # Represents an error ("not found").
        else:
            return a[i]

def find_rotation_count(a):
    """
    >>> a = [15, 22, 23, 28, 31, 38, 5, 6, 8, 10, 12]
    >>> find_rotation_count(a)
    6

    >>> a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    >>> find_rotation_count(a)
    0
    """
    n = len(a)
    low_i = 0
    high_i = n - 1
    outcome = -1  # Default to indicate not-found.
    while low_i <= high_i:
        if a[low_i] <= a[high_i]:  # Case 1
            outcome = low_i
            break
        mid_i = (low_i + high_i) // 2
        prev_i = (mid_i + n - 1) % n
        next_i = (mid_i + 1) % n
        if a[prev_i] >= a[mid_i] <= a[next_i]:  # Case 2
            outcome = mid_i
            break
        elif a[mid_i] <= a[high_i]:  # Case 3
            high_i = mid_i - 1
        elif a[low_i] <= a[mid_i]:  # Case 4
            low_i = mid_i + 1
    return outcome

if __name__ == '__main__':
    import doctest
    doctest.testmod()
