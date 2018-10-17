#!/usr/bin/env python3

# Given an integer array, find if an integer p exists in the array such that the
# number of integers greater than p in the array equals to p. If such an integer
# is found return 1 else return -1.


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, a):
        """
        >>> s = Solution()
        >>> s.solve([ 2, 5, 7 ])
        1

        >>> s.solve([5, 6, 2])
        1

        >>> s.solve([ 6, 7, 5 ])
        -1


        >>> s.solve([7, 3, 16, 10])
        1

        >>> s.solve([-1, -9, -2, -78, 0])
        1

        >>> s.solve([ 1, 2, 7, 0, 9, 3, 6, 0, 6 ])
        -1

        >>> s.solve([ -4, 7, 5, 3, 5, -4, 2, -1, -9, -8, -3, 0, 9, -7, -4, -10, -4, 2, 6, 1, -2, -3, -1, -8, 0, -8, -7, -3, 5, -1, -8, -8, 8, -1, -3, 3, 6, 1, -8, -1, 3, -9, 9, -6, 7, 8, -6, 5, 0, 3, -4, 1, -10, 6, 3, -8, 0, 6, -9, -5, -5, -6, -3, 6, -5, -4, -1, 3, 7, -6, 5, -8, -5, 4, -3, 4, -6, -7, 0, -3, -2, 6, 8, -2, -6, -7, 1, 4, 9, 2, -10, 6, -2, 9, 2, -4, -4, 4, 9, 5, 0, 4, 8, -3, -9, 7, -8, 7, 2, 2, 6, -9, -10, -4, -9, -5, -1, -6, 9, -10, -1, 1, 7, 7, 1, -9, 5, -1, -3, -3, 6, 7, 3, -4, -5, -4, -7, 9, -6, -2, 1, 2, -1, -7, 9, 0, -2, -2, 5, -10, -1, 6, -7, 8, -5, -4, 1, -9, 5, 9, -2, -6, -2, -9, 0, 3, -10, 4, -6, -6, 4, -3, 6, -7, 1, -3, -5, 9, 6, 2, 1, 7, -2, 5 ])
        -1
        """
        outcome = -1
        a = sorted(a, reverse=True)
        limit = len(a)
        # When p is zero, zero numbers are greater than zero.
        if 0 == a[0]:
            outcome = 1
        else:
            for i in range(1, limit):
                # Obs.: a repeated number does NOT count towards greater-than.
                if i == a[i] and a[i - 1] != a[i]:
                    outcome = 1
                    break
        return outcome


if __name__ == '__main__':
    import doctest
    doctest.testmod()
