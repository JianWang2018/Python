#
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# UPDATE (2016/2/13):
# The return format had been changed to zero-based indices. Please read the above updated description carefully.


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        note: use diction to solve this problem, key is the nums and value is index
        """
        if len(nums)<=1:
            raise ValueError("The length of list should be bigger than 1")
            return


        temp_dict={}
        for i in range(len(nums)):
            if target-nums[i] in temp_dict:
                return [temp_dict[target-nums[i]],i]
            else:
                temp_dict[nums[i]]=i
