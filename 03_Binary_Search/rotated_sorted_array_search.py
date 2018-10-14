#!/usr/bin/env python3

import rotated_array

"""
"""


class Solution(rotated_array.Solution):
    """
    >>> s = Solution()
    >>> s.find_rotation_count([1, 2])
    0

    >>> s.find_rotation_count([2, 1])
    1


    """

    def rotate(self, n, a):
        """
        >>> s = Solution()
        >>> s.rotate(0, [1,2])
        [1, 2]

        >>> s.rotate(1, [2, 1])
        [1, 2]
        """
        return a[-n:] + a[:-n]

    def binary_search(self, n, a, left=0, right=-1):
        """
        >>> s = Solution()
        >>> s.binary_search(0, [1, 2, 3])
        -1

        >>> s.binary_search(2, [1, 2, 3])
        1

        >>> s.binary_search(6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        6
        """
        if -1 == right:
            right = len(a)
        outcome = -1
        if left != right:
            middle = ((right - left) // 2) + left
            if n == a[middle]:
                outcome = middle
            elif n < a[middle]:
                outcome = self.binary_search(n, a, left, middle)
            elif n > a[middle]:
                outcome = self.binary_search(n, a, middle, right)
        return outcome


    def rotated_sorted_array_search(self, n, a):
        """
        >>> s = Solution()
        >>> s.rotated_sorted_array_search( 2, [2, 1])
        0
        """
        rotation = self.find_rotation_count(a)
        original = self.rotate(-rotation, a)
        original_index = self.binary_search(n, original, 0, len(a))
        index = (original_index + rotation) % len(a)
        return index


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    #s = Solution()
    #s.other()
    #s.findMin([1])
