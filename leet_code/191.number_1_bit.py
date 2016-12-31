# Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).
#
# For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.



# key: n&(n-1) each time can reduce one "1"  Think of a number in binary n = XXXXXX1000, n - 1 is XXXXXX0111. n & (n - 1)
# will be XXXXXX0000 which is just cancel the last 1
import time
class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c


# other solution
#key: can sue build in function bin and count
def hammingWeight(self, n):
    """
    :type n: int
    :rtype: int
    """
    return bin(n).count('1')

def main():
    a=11
    time_t=time.time()
    sln=Solution().hammingWeight(a)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()