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
#key:1) calculate the number of letters which has odds time occurance, , can use v&1 to define if it is odd
import collections
def longestPalindrome(self, s):
    odds = sum(v & 1 for v in collections.Counter(s).values())
    return len(s) - odds + bool(odds)



#other solution
def longestPalindrome(self, s):
    use = sum(v & ~1 for v in collections.Counter(s).values())
    return use + (use < len(s))

def longestPalindrome(self, s):
    counts = collections.Counter(s).values()
    return sum(v & ~1 for v in counts) + any(v & 1 for v in counts)


import time

def main():
    a=[4,3,2,6]
    time_t=time.time()
    sln=Solution().maxRotateFunction(a)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()