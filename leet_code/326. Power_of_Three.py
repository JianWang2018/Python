# Given an integer, write a function to determine if it is a power of three.
#
# Follow up:
# Could you do it without using any loop / recursion?

#key:1) use 3^19 wihch is the max power of 3 that is less than 2^32-1

class Solution(object):
    def isPowerOfThree(self, n):
        return n > 0 and 1162261467 % n == 0

#other solution:

# key: the
def isPowerOfThree(self, n):
    return n > 0 == 3**19 % n




import time

def main():
    a="121234"
    b="123433"
    numArray = NumArray([-2,0,3,-5,2,-1])
    time_t=time.time()
    sln=numArray.sumRange(0,4)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()