# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
#
# Example:
# Given a = 1 and b = 2, return 3.

# key: use dict to store the element and number of nums1, and find intersection in nums2.
class Solution(object):
    def guessNumber(self, n):
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) / 2
            if guess(mid) == 1:
                lo = mid + 1
            else:
                hi = mid
        return lo
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