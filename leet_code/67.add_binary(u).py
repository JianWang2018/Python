# Given two binary strings, return their sum (also a binary string).
#
# For example,
# a = "11"
# b = "1"
# Return "100".

# key: should use carry
import time
class Solution:
    def addBinary(self, a, b):
        len_a = len(a)
        len_b = len(b)
        c = 0

        while(len_a>0 or len_b>0 or c==1):


        return bin(eval('0b' + a) + eval('0b' + b))[2:]


# other solution
class Solution1:
    def addBinary(self, a, b):
        return bin(eval('0b' + a) + eval('0b' + b))[2:]

def main():
    a="1111"
    b="111"
    time_t=time.time()
    sln=Solution1().addBinary(a,b)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()