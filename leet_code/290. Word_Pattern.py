# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
#
# Examples:
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
#


# key: 1) use map, find and index function 2) in python 3.4 should use lsit () outside the map
class Solution(object):
    def wordPattern(self, pattern, str):
        s = pattern
        t = str.split(" ")
        return list(map(s.find, s)) == list(map(t.index, t))








# other solution
#Solution 2 : one-liner from @toontong: use sort() with customized compare function
#Improved version also from there:

def wordPattern(self, pattern, str):
    f = lambda s: map({}.setdefault, s, range(len(s)))
    return f(pattern) == f(str.split())
#From here:

def wordPattern(self, pattern, str):
    s = pattern
    t = str.split()
    return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)
#Thanks to zhang38 for pointing out the need to check len(s) == len(t) here.


import time

def main():
    a="abba"
    b="cat dog dog cat"
    time_t=time.time()
    sln=Solution().wordPattern(a,b)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()