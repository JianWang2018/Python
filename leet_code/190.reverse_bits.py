# Reverse bits of a given 32 bits unsigned integer.
#
# For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).
#
# Follow up:
# If this function is called many times, how would you optimize it?



# key: cansue format to define the 32 bit binary
import time
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        oribin='{0:032b}'.format(n)
        reversebin=oribin[::-1]
        return int(reversebin,2)


# other solution
#key: can use bit operator


def main():
    a=43261596
    time_t=time.time()
    sln=Solution().reverseBits(a)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()