# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
#
# Example:
# Given num = 16, return true. Given num = 5, return false.
#
# Follow up: Could you solve it without loops/recursion?

#key:1) >0 and power of 3 and can divide 3

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num>0 and num&(num-1)==0 and (num-1)%3 ==0

#other solution:
def isPowerOfFour(self, num):
        return num != 0 and num &(num-1) == 0 and num & 1431655765== num
#key:
# Consider the valid numbers within 32 bit, and turn them into binary form, they are:
#
# 1
# 100
# 10000
# 1000000
# 100000000
# 10000000000
# 1000000000000
# 100000000000000
# 10000000000000000
# 1000000000000000000
# 100000000000000000000
# 10000000000000000000000
# 1000000000000000000000000
# 100000000000000000000000000
# 10000000000000000000000000000
# 1000000000000000000000000000000
# Any other number not it the list should be considered as invalid.
# So if you XOR them altogether, you will get a mask value, which is:
#
# 1010101010101010101010101010101 (1431655765)
# Any number which is power of 4, it should be power of 2, I use num &(num-1) == 0 to make sure of that.
# Obviously 0 is not power of 4, I have to check it.
# and finally I need to check that if the number 'AND' the mask value is itself, to make sure it's in the list above.
#
# here comes the final code:
#
# return num != 0 and num &(num-1) == 0 and num & 1431655765== num
#


import time

def main():
    a=16
    time_t=time.time()
    sln=Solution().isPowerOfFour(a)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()