# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.

# key use boyer moore voting algorithm

import time
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major,counts,n=0,0,len(nums)
        for i in range(n):
            if counts ==0:
                major=nums[i];
                counts=1
            else:
                if nums[i]==major:
                    counts+=1
                else: counts -=1

        return major



# other solution


def main():
    a=[1,2,2,2,2,2,2,2,4,5,6,7,8]
    time_t=time.time()
    sln=Solution().majorityElement(a)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()