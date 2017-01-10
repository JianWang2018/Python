# Given two arrays, write a function to compute their intersection.
#
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
#
# Note:
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# Follow up:
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into
#
# the memory at once?

# key: use dict to store the element and number of nums1, and find intersection in nums2.

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict={}
        res=[]
        for i in range(len(nums1)):
            dict[nums1[i]]=dict.get(nums1[i],0)+1
        for i in range(len(nums2)):
            if dict[nums2[i]]>0 and nums2[i] in dict:
                res.append(nums2[i])
                dict[nums2[i]]-=1

        return res

#other solution:
#two pointers:

class Solution(object):
    def intersect(self, nums1, nums2):

        nums1, nums2 = sorted(nums1), sorted(nums2)
        pt1 = pt2 = 0
        res = []

        while True:
            try:
                if nums1[pt1] > nums2[pt2]:
                    pt2 += 1
                elif nums1[pt1] < nums2[pt2]:
                    pt1 += 1
                else:
                    res.append(nums1[pt1])
                    pt1 += 1
                    pt2 += 1
            except IndexError:
                break

        return res
#use dictionary to count:

class Solution(object):
    def intersect(self, nums1, nums2):

        counts = {}
        res = []

        for num in nums1:
            counts[num] = counts.get(num, 0) + 1

        for num in nums2:
            if num in counts and counts[num] > 0:
                res.append(num)
                counts[num] -= 1

        return res
#use Counter to make it cleaner:

class Solution(object):
    def intersect(self, nums1, nums2):

        counts = collections.Counter(nums1)
        res = []

        for num in nums2:
            if counts[num] > 0:
                res += num,
                counts[num] -= 1

        return res

# key: map counter and &
def intersect(self, nums1, nums2):
    a, b = map(collections.Counter, (nums1, nums2))
    return list((a & b).elements())

def intersect(self, nums1, nums2):
    C = collections.Counter
    return list((C(nums1) & C(nums2)).elements())

def intersect(self, nums1, nums2):
    return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())



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