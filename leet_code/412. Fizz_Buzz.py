# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
#
# This is case sensitive, for example "Aa" is not considered a palindrome here.
#
# Note:
# Assume the length of given string will not exceed 1,010.
#
# Example:
#
# Input:
# "abccccdd"
#
# Output:
# 7
#
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
#key:1)
import collections
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        for i in range(n):
            if not(i+1)%3 and not (i+1)%5:
                res.append("FizzBuzz")
            elif not (i+1)%3:
                res.append("Fizz")
            elif not (i+1)%5:
                res.append("Buzz")
            else:
                res.append(str(i+1))
        return res



#other solution
def fizzBuzz(self, n):
    return['FizzBuzz'[i%-3&-4:i%-5&8^12]or`i`for i in range(1,n+1)]

def fizzBuzz(self, n):
    return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]


import time

def main():
    a=[4,3,2,6]
    time_t=time.time()
    sln=Solution().maxRotateFunction(a)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()