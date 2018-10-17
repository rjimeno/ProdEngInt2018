#!/usr/bin/env python3


class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        """
        >>> s = Solution()
        >>> s.prettyPrint(1)
        [[1]]

        >>> s.prettyPrint(2)
        [[2, 2, 2], [2, 1, 2], [2, 2, 2]]

        >>> s = Solution()
        >>> s.prettyPrint(3)
        [[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]

        """
        # rjimeno copied the following from gersakbogdan's comment (on 18 Apr 2016) at:
        # http://qa.geeksforgeeks.org/3686/qa.geeksforgeeks.org/3686/print-concentric-rectangular-pattern-in-a-2d-matrix.html
        size = 2 * A - 1
        array = [[0 for x in range(size)] for y in range(size)]
        for i in range(0, size):
            for j in range(i, size - i):
                array[i][j] = A - i
                array[j][i] = A - i
                array[size - 1 - i][j] = A - i
                array[j][size - 1 - i] = A - i
        r = []
        for i in range(0, size):
            r.append(array[i])
        return r


if __name__ == '__main__':
    import doctest
    doctest.testmod()
