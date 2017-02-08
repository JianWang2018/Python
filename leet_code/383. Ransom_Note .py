# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
#
# Each letter in the magazine string can only be used once in your ransom note.
#
# Note:
# You may assume that both strings contain only lowercase letters.
#
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true

# key: the nunber of element in ransom should be less than in magazine
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dict={}
        for i in range(len(magazine)):
            dict[magazine[i]]=dict.get(magazine[i],0)+1
        for i in range(len(ransomNote)):
            if not (ransomNote[i] in dict):
                return False
            elif dict[ransomNote[i]]<=0:
                return False
            else :dict[ransomNote[i]]-=1

        return True
#other solution:
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        return all(ransomNote.count(c)<=magazine.count(c) for c in ransomNote)
#Based on the trivial method, we can use set to avoid some duplication. This works amazingly fast for the test cases.

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        return all(ransomNote.count(c)<=magazine.count(c) for c in set(ransomNote))
#Or even exploiting the given condition that there are only small letters:

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        return all(ransomNote.count(c)<=magazine.count(c) for c in string.ascii_lowercase)
#It gave me 80 ms, the fastest method listed here.

#=================================

Ok, here come some more "proper" ways. Proper, as in they don't assume anything about the alphabet.

#Proper Method 1: Use Counter and compare letters' counts:

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        c1, c2 = collections.Counter(ransomNote), collections.Counter(magazine)
        return all(k in c2 and c2[k]>=c1[k] for k in c1)
#Proper Method 2: Sort the strings and do a traversal.

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        s, i = sorted(ransomNote), 0
        for c in sorted(magazine):
            i += i<len(s) and s[i]==c
        return i==len(s)
#Longer but easier to understand version. There is an extra check c>s1[i] for faster termination, but it's not really faster for the test cases here.

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        s1, s2, i = sorted(ransomNote), sorted(magazine), 0
        for c in s2:
            if i==len(s1) or c>s1[i]:
                break
            if c==s1[i]:
                i += 1
        return i==len(s1)

import time

def main():
    a="aa"
    b="ab"
    time_t=time.time()
    sln=Solution().canConstruct(a,b)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()