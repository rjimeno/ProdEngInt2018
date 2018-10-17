#!/usr/bin/env python3

"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

    Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
    The solution set must not contain duplicate triplets.

    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
"""

class Solution:

    def threeSum(self, a):
        """
        >>> s = Solution()
        >>> s.threeSum([0])
        []

        >>> s.threeSum([4, -4])
        []

        >>> s.threeSum([-1, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 1])
        [(-1, 0, 1), (0, 0, 0)]

        >>> a = [-1, 0, 1, 2, -1, -4]
        >>> s.threeSum(a)
        [(-1, -1, 2), (-1, 0, 1)]

        >>> a = [ 1, -4, 0, 0, 5, -5, 1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3 ]
        >>> s.threeSum(a)
        [(-2, 1, 1), (-4, 1, 3), (-4, 0, 4), (-4, -1, 5), (-3, -1, 4), (-3, 0, 3), (-1, 0, 1), (0, 0, 0), (-3, -2, 5), (-5, 1, 4), (-2, -1, 3), (-5, 0, 5)]
        """
        if 1 <= len(a) <= 2:
            return []
        a.sort()
        solution_set = set()
        for i in range(len(a) - 2):
            j = i + 1
            k = len(a) - 1
            while j < k:
                s = (a[i],  a[j], a[k])
                if sum(s) < 0:
                    j += 1
                elif 0 < sum(s):
                    k -= 1
                else:
                    solution_set.add(s)
                    j += 1
                    k -= 1
                    while j < k and a[j - 1] == a[j]:
                        j += 1
                    while j < k and a[k] == a[k + 1]:
                        k -=1
        return list(solution_set)


if __name__ == '__main_)':
    import doctest
    doctest.testmod()
