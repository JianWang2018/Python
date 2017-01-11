# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
#
# Example:
# Given a = 1 and b = 2, return 3.

# key: use dict to store the element and number of nums1, and find intersection in nums2.
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000
        MASK = 0x100000000
        while b:
            a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)
#other solution:
#two pointers:

import time

def main():
    a=1
    b=3
    time_t=time.time()
    sln=Solution().getSum(a,b)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()