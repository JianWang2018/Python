# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
#
# For example,
# Given "egg", "add", return true.
#
# Given "foo", "bar", return false.
#
# Given "paper", "title", return true.

# # key: primes[i * i: n: i] = [False] * len(primes[i * i: n: i])

import time
class Solution(object):
    def isIsomorphic1(self, s, t):
        d1, d2 = {}, {}
        for i, val in enumerate(s):
            d1[val] = d1.get(val, []) + [i] # here get can give a initial value [] if the key is not found
        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]
        return sorted(d1.values()) == sorted(d2.values())


# other solution
#key: can use set to store past value


def isIsomorphic2(self, s, t):
    d1, d2 = [[] for _ in xrange(256)], [[] for _ in xrange(256)]
    for i, val in enumerate(s):
        d1[ord(val)].append(i)
    for i, val in enumerate(t):
        d2[ord(val)].append(i)
    return sorted(d1) == sorted(d2)

def isIsomorphic3(self, s, t):
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))

def isIsomorphic4(self, s, t):
    return [s.find(i) for i in s] == [t.find(j) for j in t]

def isIsomorphic5(self, s, t):
    return map(s.find, s) == map(t.find, t)

def isIsomorphic(self, s, t):
    d1, d2 = [0 for _ in xrange(256)], [0 for _ in xrange(256)]
    for i in xrange(len(s)):
        if d1[ord(s[i])] != d2[ord(t[i])]:
            return False
        d1[ord(s[i])] = i+1
        d2[ord(t[i])] = i+1
    return True



def main():
    a="eeegdgaad"
    b="gggdfdaaf"
    time_t=time.time()
    sln=Solution().isIsomorphic1(a,b)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()