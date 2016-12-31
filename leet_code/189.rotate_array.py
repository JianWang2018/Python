# Rotate an array of n elements to the right by k steps.
#
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
#
# Note:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
#
# [show hint]
#
# Hint:
# Could you do it in-place with O(1) extra space?

# key: can use negative index
import time
class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return nums


# other solution


def main():
    a=[1,2,3,4,5,6,6,7]
    b=3
    time_t=time.time()
    sln=Solution().rotate(a,b)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()