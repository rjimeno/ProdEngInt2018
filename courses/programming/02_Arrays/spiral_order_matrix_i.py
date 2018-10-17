#!/usr/bin/env python3

# Given a matrix of m * n elements (m rows, n columns), return all elements
# of the matrix in spiral order.

class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, a):
        """
        >>> s = Solution()
        >>> s.spiralOrder([[ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]])
        [1, 2, 3, 6, 9, 8, 7, 4, 5]
        """
        T=0
        B=len(a)-1
        L=0
        R=len(a[0])-1
        result=[]
        dir = 0  # Four "directions" are possible (only).
        while T<=B and L<=R:
            if dir == 0:
                for i in range(L, R+1, +1):
                    result.append(a[T][i])
                T += 1
                dir = 1
            elif dir == 1:
                for i in range(T, B+1, +1):
                    result.append(a[i][R])
                R -= 1
                dir = 2
            elif dir == 2:
                for i in range(R, L-1, -1):
                    result.append(a[B][i])
                B -= 1
                dir = 3
            else:  #dir==3
                for i in range(B, T-1, -1):
                    result.append(a[i][L])
                L += 1
                dir = 0
        return(result)