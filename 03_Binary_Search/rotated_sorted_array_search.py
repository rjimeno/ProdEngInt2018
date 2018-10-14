#!/usr/bin/env python3


"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 ).

You are given a target value to search. If found in the array, return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Input : [4 5 6 7 0 1 2] and target = 4
Output : 0

        NOTE : Think about the case when there are duplicates. Does your
        current solution work? How does the time complexity change?*
"""


class Solution:
    def search(self, a, n):
        """
        >>> s = Solution()
        >>> s.search([ 101, 103, 106, 109, 158, 164, 182, 187, 202, 205, 2, 3, 32, 57, 69, 74, 81, 99, 100 ], 202)
        8
        >>> s.search([ 186, 192, 193, 202, 204, 2, 3, 6, 10, 11, 12, 17, 21, 28, 29, 30, 31, 32, 37, 38, 39, 40, 41, 47, 49, 50, 51, 52, 55, 57, 58, 59, 60, 65, 67, 68, 71, 72, 74, 77, 78, 80, 82, 83, 88, 89, 90, 94, 100, 107, 108, 109, 111, 112, 114, 115, 116, 118, 119, 121, 123, 124, 126, 129, 133, 134, 135, 137, 138, 144, 147, 148, 150, 151, 154, 156, 159, 161, 163, 165, 166, 167, 168, 169, 174, 178, 180, 182, 183, 185 ], 143)
        -1
        """
        return self.binary_search(n, a)

    def find_rotation_count(self, a):
        """
        >>> s = Solution()
        >>> s.find_rotation_count([1, 2])
        0

        >>> s.find_rotation_count([2, 1])
        1

        >>> a = [15, 22, 23, 28, 31, 38, 5, 6, 8, 10, 12]
        >>> s.find_rotation_count(a)
        6

        >>> a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        >>> s.find_rotation_count(a)
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

    def rotate(self, n, a):
        """
        >>> s = Solution()
        >>> s.rotate(0, [1,2])
        [1, 2]

        >>> s.rotate(1, [2, 1])
        [1, 2]
        """
        return a[-n:] + a[:-n]

    def binary_search(self, n, a):
        """
        >>> s = Solution()
        >>> s.binary_search(0, [1, 2, 3])
        -1

        >>> s.binary_search(2, [1, 2, 3])
        1

        >>> s.binary_search(6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        6
        """
        low, high = 0, len(a) - 1
        outcome = -1
        while low <= high:
            mid = (low + high) // 2
            if a[mid] == n:
                outcome = mid
                break
            elif n < a[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return outcome

    def rotated_sorted_array_search(self, n, a):
        """
        >>> s = Solution()
        >>> s.rotated_sorted_array_search( 2, [2, 1])
        0
        """
        rotation = self.find_rotation_count(a)
        original = self.rotate(-rotation, a)
        original_index = self.binary_search(n, original)
        index = (original_index + rotation) % len(a)
        return index


if __name__ == '__main__':
    import doctest
    doctest.testmod()
