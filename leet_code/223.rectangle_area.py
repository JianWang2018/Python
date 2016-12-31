# Find the total area covered by two rectilinear rectangles in a 2D plane.
#
# Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
#
# Rectangle Area
# Assume that the total area is never beyond the maximum possible value of int.

# key: the overlap is the min of top right minus the max of bottom left
import time
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
   def computeArea(self, A, B, C, D, E, F, G, H):
        overlap = max(min(C,G)-max(A,E), 0)*max(min(D,H)-max(B,F), 0)
        return (A-C)*(B-D) + (E-G)*(F-H) - overlap



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