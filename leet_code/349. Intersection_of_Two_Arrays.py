# Given two arrays, write a function to compute their intersection.
#
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
#
# Note:
# Each element in the result must be unique.
# The result can be in any order.

# key: use:  brute force
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums1:
            if i not in res and i in nums2:
                res.append(i)

        return res

#other solution:

# use hash table,use dict/hashmap to record all nums appeared in the first list, and then check if there are nums in the
# second list have appeared in the map.
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        map = {}
        for i in nums1:
            map[i] = map[i]+1 if i in map else 1
        for j in nums2:
            if j in map and map[j] > 0:
                res.append(j)
                map[j] = 0

        return res



import time

def main():
    a="hello"
    b="hoolll"
    time_t=time.time()
    sln=Solution().intersection(a,b)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()