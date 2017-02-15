# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
#     For example, given array S = {-1 2 1 -4}, and target = 1.
#
#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Subscribe to see which companies asked this question.

# key:similar with 3 sum, just choose the closet one each time.

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result=[]
        if len(nums)<3:
            return []
        for i in range (len(nums)):
            # if the element is same with the former one, we move to the next one
            # since this situation has already been considered
            # note that it is very import to have i>0, since nums[-1] also exists
            if i >0 and nums[i]==nums[i-1]:
                continue
            else:
                left, right=i+1,len(nums)-1
                while left<right:
                    s=nums[i]+nums[left]+nums[right]
                    if s>0:
                        right-=1
                    elif s<0:
                        left+=1
                    else:
                        result.append([nums[i],nums[left],nums[right]])
                        #next move the cursor if the value of left and right is
                        #same
                        # here should be careful that left should be less than
                        #len(nums)-1 and right should be greater than 1
                        while left< len(nums)-1 and nums[left+1]==nums[left]:
                            left+=1
                        while right >1 and nums[right-1]==nums[right]:
                            right-=1
                        left+=1
                        right-=1
        return result

class Solution1:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            j, k = i+1, len(num) - 1
            while j < k:
                sum = num[i] + num[j] + num[k]
                if sum == target:
                    return sum

                if abs(sum - target) < abs(result - target):
                    result = sum

                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1

        return result
#
# def main():
#     s="   +123"
#     sln=Solution().myAtoi(s)
#     print(sln)
#
# if __name__=="__main__":
#     main()