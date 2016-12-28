# Given numRows, generate the first numRows of Pascal's triangle.
#
# For example, given numRows = 5,
# Return
#
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

# key: explanation: Any row can be constructed using the offset sum of the previous row. Example:

 #    1 3 3 1 0
 # +  0 1 3 3 1
 # =  1 4 6 4 1

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import time
class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    # 1:27
    def generate(self, numRows):
            res = [[1]]
            for i in range(1, numRows):
                res.append([x+y for x,y in  zip(res[-1] + [0], [0] + res[-1])])
            return res[:numRows]


# other good solution:


def main():
    n=5
    time_t=time.time()
    sln=Solution().generate(n)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()