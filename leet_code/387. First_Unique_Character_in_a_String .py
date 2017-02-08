# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.

# key: the nunber of element in ransom should be less than in magazine
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict={}
        for i in range(len(s)):
            dict[s[i]]=dict.get(s[i],0)+1
        for i in range(len(s)):
            if dict[s[i]]==1: return i

        return -1



#other solution

class Solution1(object):
    def firstUniqChar(self, s):
        return min([s.find(c) for c in string.ascii_lowercase if s.count(c)==1] or [-1])

class Solution1(object):
    def firstUniqChar(self, s):
        return min([s.find(c) for c,v in collections.Counter(s).iteritems() if v==1] or [-1])

# key: use find and rfind of str, rfind is find the element from right to left, find is from left to right

class Solution1(object):
    def firstUniqChar(self, str1):
        """
        :type s: str
        :rtype: int
        """
        for x in str1:
            if str1.find(x)==str1.rfind(x):
                return str1.find(x)
        return -1
import time

def main():
    a="asacceasasddf"
    time_t=time.time()
    sln=Solution().firstUniqChar(a)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()