# Given an index k, return the kth row of the Pascal's triangle.
#
# For example, given k = 3,
# Return [1,3,3,1].
#
# Note:
# Could you optimize your algorithm to use only O(k) extra space?

# key: explanation: Any row can be constructed using the offset sum of the previous row. Example:

 #    1 3 3 1 0
 # +  0 1 3 3 1
 # =  1 4 6 4 1


import time

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row

# other good solution:
# key: can use map to build link of left and right node with maxDepth



def main():
    n=5
    time_t=time.time()
    sln=Solution().getRow(n)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()