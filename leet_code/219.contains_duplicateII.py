# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such
#
# that nums[i] = nums[j] and the difference between i and j is at most k.

# use dict to store the num as key and index as val
import time
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False



# other solution
#key: use set and len tnd if duplicate
class Solution1(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums))!=len(nums)



def main():
    a=[3,3]
    time_t=time.time()
    sln=Solution().containsDuplicate(a)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()