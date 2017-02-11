# Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).
#
# Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).
#
# Example:
# Input:
# [[0,0],[1,0],[2,0]]
#
# Output:
# 2
#
# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

#key:for each point, create a hashmap and count all points with same distance. If for a point p, there are k points with
# distance d, number of boomerangs corresponding to that are k*(k-1). Keep adding these to get the final result.
import collections
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for p in points:
            cmap = {}
            for q in points:
                f = p[0]-q[0]
                s = p[1]-q[1]
                cmap[f*f + s*s] = 1 + cmap.get(f*f + s*s, 0)
            for k in cmap:
                res += cmap[k] * (cmap[k] -1)
        return res




#other solution
# key: use quadratic formula
def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int((1+8*n)**0.5 - 1) / 2
import time

def main():
    a=100

    time_t=time.time()
    sln=Solution().arrangeCoins(a)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()