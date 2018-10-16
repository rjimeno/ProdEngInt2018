#!/usr/bin/env python3

"""
DOES NOT WORK JUST YET. Work In Progress (WIP) only!
"""

W = 2

def i_p(t, s):
    tabs = " " * t
    print(tabs + s)


class Solution:
    # @param s : string
    # @return None
    def prettyJSON(self, a):
        """
        >>> s = Solution()
        >>> s.prettyJSON('{}')
        {
        }

        >>> s.prettyJSON('{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}')
        {
            A:"B",
            C:
            {
                D:"E",
                F:
                {
                    G:"H",
                    I:"J"
                }
            }
        }
        """
        t = 0
        i = 0
        while i < len(a):
            if '{' == a[i]:
                i_p(t, '{')
                t += W
            elif '}' == a[i]:
                t -= W
                i_p(t, '}')
            i += 1
        return None

if __name__ == '__main__':
    import doctest
    doctest.testmod()
