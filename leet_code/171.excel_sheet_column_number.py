# Related to question Excel Sheet Column Title
#
# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28


# can use reduce to calculate a*26**n+ b*26**(n-1)....

import time
import functools
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return functools.reduce(lambda x, y : x * 26 + y, [ord(c) - 64 for c in list(s)])




# other solution


def main():
    a="AAA"
    time_t=time.time()
    sln=Solution().titleToNumber(a)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()