#!/usr/bin/env python3

# I copied max_special_product's solution from interviewbit.
# My only contribution are the tests.


class Solution:
    # @param A : list of integers
    # @return an integer
    """
    >>> s = Solution()
    >>> s.maxSpecialProduct([7, 5, 7, 9, 8, 7])
    0

    >>> s.maxSpecialProduct([6, 7, 9, 5, 5, 8])
    10

    >>> s.maxSpecialProduct([ 5, 9, 6, 8, 6, 4, 6, 9, 5, 4, 9 ])
    80
    """
    def max_special_product(self, a_a):
        ans = 0
        st = []
        for i, a in enumerate(a_a):
            while st and a >= a_a[st[-1]]:
                j = st.pop()
                if st and a_a[j] < a:
                    ans = max(ans, st[-1] * i)
            st.append(i)
        return ans % 1000000007

    maxSpecialProduct = max_special_product


if __name__ == '__main__':
    import doctest
    doctest.testmod()
