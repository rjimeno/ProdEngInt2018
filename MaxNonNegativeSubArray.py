#!/usr/bin/env python3

"""
Find out the maximum sub-array of non negative numbers from an array.
The sub-array should be continuous. That is, a sub-array created by choosing
the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the
sub-array. Sub-array A is greater than sub-array B if sum(A) > sum(B).

Example:

A : [1, 2, 5, -7, 2, 3]
The two sub-arrays are [1, 2, 5] [2, 3].
The answer is [1, 2, 5] as its sum is larger than [2, 3]

NOTE: If there is a tie, then compare with segment's length and return segment which has maximum length
NOTE 2: If there is still a tie, then return the segment with minimum starting index

>>> A = [1, 2, 5, -7, 2, 3]
>>> maxset(A)
[1, 2, 5]

#>>> A = [1, 2, 5, -7, 2, 2, 2, 2]
#>>> maxset(A)
#[2, 2, 2, 2]

>>> A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
>>> maxset(A)
[4, -1, 2, 1]
"""


class Solution:
    # @param A : tuple of integers
    # @return an integer
    """
    >>> s = Solution()
    >>> s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4 ])
    6

    >>> s.maxSubArray([-500])
    -500

    >>> s.maxSubArray([-163, -20])
    -20
    """
    def maxSubArray(self, A):
        return(sum(maxset(A)))


def maxset2(a_int_l):
    max_list = [ a_int_l[0] ]
    i = 0
    while 0 <= i <= len(a_int_l):
        j = i
        for j in range(i, len(a_int_l)):
            if sum(max_list) < sum(a_int_l[i:j + 1]):
                max_list = a_int_l[i:j + 1]
            if 0 < sum(a_int_l[i:j + 1]):
                pass
            else:
                i = j + 1
        i += 1
    return max_list


maxset = maxset2


def main():
    s = Solution()

    a_int_l = [1, 2, 5, -7, 2, 3]
    print(maxset(a_int_l))
    print(s.maxSubArray(a_int_l))


    a_int_l = [1, 2, 5, -7, 2, 2, 2, 2]
    print(maxset(a_int_l))
    print(s.maxSubArray(a_int_l))

    a_int_l = [ -2, 1, -3, 4, -1, 2, 1, -5, 4 ]
    print(s.maxSubArray(a_int_l))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
