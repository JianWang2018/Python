# Given an integer n, return the number of trailing zeroes in n!.
#
# Note: Your solution should be in logarithmic time complexity.


# key: 10 is the product of 2 and 5. In n!, we need to know how many 2 and 5, and the number of zeros is the minimum of the number of 2 and the number of 5.
#
# Since multiple of 2 is more than multiple of 5, the number of zeros is dominant by the number of 5.
#
# Here we expand
#
#   2147483647!
# =2 * 3 * ...* 5 ... *10 ... 15* ... * 25 ... * 50 ... * 125 ... * 250...
# =2 * 3 * ...* 5 ... * (5^1*2)...(5^1*3)...*(5^2*1)...*(5^2*2)...*(5^3*1)...*(5^3*2)... (Equation 1)
# We just count the number of 5 in Equation 1.
#
# Multiple of 5 provides one 5, multiple of 25 provides two 5 and so on.
#
# Note the duplication: multiple of 25 is also multiple of 5, so multiple of 25 only provides one extra 5.
#
# Here is the basic solution:
#
# return n/5 + n/25 + n/125 + n/625 + n/3125+...;

import time
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        m= 5
        res= 0
        while (n//m != 0 ):
            res =res +n//m
            m*=5
        return res

# other solution


def main():
    a=200
    time_t=time.time()
    sln=Solution().trailingZeroes(a)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()