# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
#
# The order of output does not matter.
#
# Example 1:
#
# Input:
# s: "cbaebabacd" p: "abc"
#
# Output:
# [0, 6]
#
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:
#
# Input:
# s: "abab" p: "ab"
#
# Output:
# [0, 1, 2]
#
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

#key:1) current is space and previous is not space
#2) should add a space at the end of the string
import collections
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s+" "
        print(s)
        res=0
        for i in range(1,len(s)):
            if s[i]==" " and s[i-1]!=" ":
                res+=1
        return res






#other solution
# key: can use split
class Solution(object):
def countSegments(self, s):
"""
:type s: str
:rtype: int
"""
return len(s.split())
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