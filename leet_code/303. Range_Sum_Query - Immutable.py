# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
#
# Example:
# Given nums = [-2, 0, 3, -5, 2, -1]
#
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# Note:
# You may assume that the array does not change.
# There are many calls to sumRange function.

#key:1)The idea is fairly straightforward: create an array accu that stores the accumulated sum for nums such that accu[i] = nums[0]
# + ... + nums[i - 1] in the initializer of NumArray. Then just return accu[j + 1] - accu[i] in sumRange. You may try the
# example in the problem statement to convince yourself of this idea.
#2) be careful of overflow if use common plus method
# 3) accumulate should start from 0 and use nums_sum[j+1]-self.nums_sum[i], otherwise, it will be wrong when i==0

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums_sum=[0]
        for i in range(0,len(nums)):
            self.nums_sum.append(self.nums_sum[-1]+nums[i])



    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.nums_sum[j+1]-self.nums_sum[i]

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)

#other solution:

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.accu = [0]
        for num in nums:
            self.accu += self.accu[-1] + num,

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.accu[j + 1] - self.accu[i]






import time

def main():
    a="121234"
    b="123433"
    numArray = NumArray([-2,0,3,-5,2,-1])
    time_t=time.time()
    sln=numArray.sumRange(0,4)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()