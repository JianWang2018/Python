# Given an array of integers, find if the array contains any duplicates. Your function should return true if any value
# appears at least twice in the array, and it should return false if every element is distinct.

# key: if sorted then O(N), else can use hash table to have O(n) time and o(n) space complexity
# key, can not use dict should use set, otherwise it will time out
import time
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        numSet=set()
        for num in nums:
            if num in numSet:
                return True
            numSet.add(num)
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