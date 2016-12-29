# Compare two version numbers version1 and version2.
# If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
#
# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.
#
# Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
# key:
# the idea is if you switch head, the possible difference between length would be countered.
# On the second traversal, they either hit or miss.
# if they meet, pa or pb would be the node we are looking for,
# if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them is the same,None

import time

class Solution(object):
    def compareVersion(self, version1, version2):
        versions1 = [int(v) for v in version1.split(".")]
        versions2 = [int(v) for v in version2.split(".")]
        for i in range(max(len(versions1),len(versions2))):
            v1 = versions1[i] if i < len(versions1) else 0
            v2 = versions2[i] if i < len(versions2) else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1;
        return 0;


# other solution
#Solution 1: Pad with izip_longest with fillvalue=0

def compareVersion(self, version1, version2):
    splits = (map(int, v.split('.')) for v in (version1, version2))
    return cmp(*zip(*itertools.izip_longest(*splits, fillvalue=0)))
#Solution 2: Pad with [0] * lengthDifference

def compareVersion(self, version1, version2):
    v1, v2 = (map(int, v.split('.')) for v in (version1, version2))
    d = len(v2) - len(v1)
    return cmp(v1 + [0]*d, v2 + [0]*-d)
#Solution 3: Recursive, add zeros on the fly

def compareVersion(self, version1, version2):
    main1, _, rest1 = ('0' + version1).partition('.')
    main2, _, rest2 = ('0' + version2).partition('.')
    return cmp(int(main1), int(main2)) or \
           len(rest1+rest2) and self.compareVersion(rest1, rest2)

def main():
    a="22.11"
    b="11.21"
    time_t=time.time()
    sln=Solution().compareVersion(a,b)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()