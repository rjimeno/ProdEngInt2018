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

>>> A = [1, 2, 5, -7, 2, 2, 2, 2]
>>> maxset(A)
[2, 2, 2, 2]
"""


def maxset(a_int_l):
    maximum = [a_int_l[0]]
    i = 0
    while i < len(a_int_l):
        j = i
        while j < len(a_int_l):
            if a_int_l[j] > 0:
                curr = a_int_l[i:j + 1]
                if sum(maximum) < sum(curr):  # We just found a new maximum
                    maximum = curr
                elif sum(maximum) == sum(curr):
                    if len(maximum) < len(curr):
                        maximum = curr
                    elif maximum[i] > curr[i]:
                        maximum = curr
            else:
                break
            j += 1
        i = j + 1
    return maximum


def main():
    a_int_l = [1, 2, 5, -7, 2, 3]
    print(maxset(a_int_l))

    a_int_l = [1, 2, 5, -7, 2, 2, 2, 2]
    print(maxset(a_int_l))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
