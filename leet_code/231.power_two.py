# Find the total area covered by two rectilinear rectangles in a 2D plane.
#
# Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
#
# Rectangle Area
# Assume that the total area is never beyond the maximum possible value of int.

# use dict to store the num as key and index as val
import time
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (not n&(n-1)) and (n!=0)



# other solution



def main():
    a=20
    time_t=time.time()
    sln=Solution().isPowerOfTwo(a)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()