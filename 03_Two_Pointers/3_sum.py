#!/usr/bin/env python3

"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers.

Assume that there will only be one solution

Example:
given array S = {-1 2 1 -4},
and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
"""
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, a, t):
        """
        >>> s = Solution()

        >>> s.threeSumClosest([1, 2, -1], 2)
        2

        #>>> s.threeSumClosest([-1, 2, 1, -4], 0)
        #-1

        >>> s.threeSumClosest([-1, 2, 1, -4], 1)
        2

        >>> s.threeSumClosest([-1, 2, 1, -4], 3)
        2

        """
        if len(a) < 3:
            return 1000000000 # Magic number.
        elif len(a) == 3:
            return sum(a)
        a.sort()
        # The following number represents a magnitude and should never be smaller than zero.
        candidate = None
        smallest_difference = float('inf')
        for i in range(len(a) - 2):
            top = len(a) - 1
            bottom = i + 1
            s1 = a[i]
            s2 = a[top]
            s3 = a[bottom]
            total =  s1 + s2 + s3
            while bottom < top:  # and 0 < smallest_difference:
                total = s1 + s2 + s3
                if t < total:
                    if total - t < smallest_difference:
                        smallest_difference = total - t
                    top -= 1
                    s2 = a[top]
                    continue
                elif total < t:
                    if t - total < smallest_difference:
                        smallest_difference = t - total
                    bottom += 1
                    s3 = a[bottom]
                    continue
                else:
                    # An exact sum was found and nothing else matters.
                    return t
            # At this point, total != t for every sensible s2 & s3; let's try the next s1.
        # At this point, there was no exact match anywhere; so, let's use the smallest difference instead:
        return total

if __name__ == '__main__':
    import doctest
    doctest.testmod()
