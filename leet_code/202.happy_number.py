# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
#
# Example: 19 is a happy number
#
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1


# # key: Using fact all numbers in [2, 6] are not happy (and all not happy numbers end on a cycle that hits this interval):

import time
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n >6:
            next =0
            while (n):
                next+=(n%10)*(n%10)
                n//=10
            n=next
        return n==1

# other solution
#key: can use set to store past value

def isHappy(self, n):
    """
    :type n: int
    :rtype: bool
    """
    mem = set()
    while n != 1:
        n = sum([int(i)**2 for i in str(n)])
        if n not in mem:
            mem.add(n)
        else:
            return False
    return True



def main():
    a=19
    time_t=time.time()
    sln=Solution().isHappy(a)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()