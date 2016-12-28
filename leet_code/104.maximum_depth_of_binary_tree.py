# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# key: use recursion of left and right node and plus one

import time
class Solution:
  def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        ldepth=self.maxDepth(root.left)
        rdepth=self.maxDepth(root.right)
        return max(ldepth,rdepth)+1



# other good solution:
# key: can use map to build link of left and right node with maxDepth
def maxDepth(self, root):
    return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0