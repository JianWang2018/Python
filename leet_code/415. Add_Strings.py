# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.


#key:1)set will be sorted automatically
#2) set do not have index, so need to remove the max for second times
import collections
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i=len(num1)-1
        j=len(num2) -1
        carry=0
        res=""
        while i>=0 or j>=0 or carry:
            sum=0
            if i>=0:
                sum+=int(num1[i])
                i-=1
            if(j>=0):
                sum+=int(num2[j])
                j-=1
            sum+= carry
            carry=sum//10
            sum%=10
            res=res+str(sum)
        return res[::-1]




#other solution
# key: can use zip longest
from itertools import izip_longest
class Solution(object):
    def addStrings(self, num1, num2):
        res, c = "", 0
        for (x, y) in izip_longest(num1[::-1], num2[::-1], fillvalue='0'):
            s = (int(x) + int(y) + c)
            d, c = s % 10, int(s / 10)
            res = str(d) + res

        if c > 0: res = str(c) + res

        return res
import time

def main():
    a="220"
    b="11"
    time_t=time.time()
    sln=Solution().addStrings(a,b)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()