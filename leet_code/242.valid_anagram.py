# Given two strings s and t, write a function to determine if t is an anagram of s.
#
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
#
# Note:
# You may assume the string contains only lowercase alphabets.

# key: anagram is the order different but the content same
import time
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1,dic2 ={},{}

        for item in s:
            dic1[item]=dic1.get(item,0)+1
        for item in t:
            dic2[item]=dic2.get(item,0)+1
        return dic1==dic2



# other solution
# key:can use sorted

def isAnagram2(self, s, t):
    dic1, dic2 = [0]*26, [0]*26
    for item in s:
        dic1[ord(item)-ord('a')] += 1
    for item in t:
        dic2[ord(item)-ord('a')] += 1
    return dic1 == dic2

def isAnagram3(self, s, t):
    return sorted(s) == sorted(t)

def main():
    a="asaba"
    b="abasa"
    time_t=time.time()
    sln=Solution().isAnagram(a,b)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()