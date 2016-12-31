# Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).
#
# For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.



# # key: dp problem
# f(0) = nums[0]
# f(1) = max(num[0], num[1])
# f(k) = max( f(k-2) + nums[k], f(k-1) )

import time
class Solution:
    # @param n, an integer
    # @return an integer
    class Solution:

        def rob(self, nums):

            last, now = 0, 0

            for i in nums: last, now = now, max(last + i, now)

            return now

# other solution
#key: can sue build in function bin and count





def main():
    a=11
    time_t=time.time()
    sln=Solution().hammingWeight(a)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()