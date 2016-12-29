# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#
# For example:
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB

# key:Let's see the relationship between the Excel sheet column title and the number:

# A   1     AA    26+ 1     BA  2×26+ 1     ...     ZA  26×26+ 1     AAA  1×26²+1×26+ 1
# B   2     AB    26+ 2     BB  2×26+ 2     ...     ZB  26×26+ 2     AAB  1×26²+1×26+ 2
# .   .     ..    .....     ..  .......     ...     ..  ........     ...  .............
# .   .     ..    .....     ..  .......     ...     ..  ........     ...  .............
# .   .     ..    .....     ..  .......     ...     ..  ........     ...  .............
# Z  26     AZ    26+26     BZ  2×26+26     ...     ZZ  26×26+26     AAZ  1×26²+1×26+26
# Now we can see that ABCD＝A×26³＋B×26²＋C×26¹＋D＝1×26³＋2×26²＋3×26¹＋4
#
# But how to get the column title from the number? We can't simply use the n%26 method because:
#
# ZZZZ＝Z×26³＋Z×26²＋Z×26¹＋Z＝26×26³＋26×26²＋26×26¹＋26
#
# We can use (n-1)%26 instead, then we get a number range from 0 to 25.

# key: use (n-1)% 26, chr() return char based on ascII, ord() return ascII based on chr

import time

class Solution(object):
    def convertToTitle(self,num):
        result = []
        while num > 0:
            result.append(chr((num-1)%26+ord('A')))
            num = (num-1) // 26
        result.reverse()
        return ''.join(result)

# other solution


def main():
    a=111
    time_t=time.time()
    sln=Solution().convertToTitle(a)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()