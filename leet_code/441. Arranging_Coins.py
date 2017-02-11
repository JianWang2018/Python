# You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
#
# Given n, find the total number of full staircase rows that can be formed.
#
# n is a non-negative integer and fits within the range of a 32-bit signed integer.
#
# Example 1:
#
# n = 5
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
#
# Because the 3rd row is incomplete, we return 2.
# Example 2:
#
# n = 8
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
#
# Because the 4th row is incomplete, we return 3.

#key:1) use binary search
#2) use (n+1)n/2
# 3) mid= start+(end-start)/2 this one will not over flow
import collections
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        start=0
        end=n
        mid=0
        while start<=end:
            mid=int(start+(end-start)/2)
            if (0.5*mid**2+0.5*mid)<=n:
                start=mid+1
            else: end =mid -1
        return start-1




#other solution
# key: use quadratic formula
def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int((1+8*n)**0.5 - 1) / 2
import time

def main():
    a=100

    time_t=time.time()
    sln=Solution().arrangeCoins(a)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()