# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# key: We need to add the smaller one of the child depths - except if that's zero, then add the larger one.
class Solution(object):
    def minDepth(self, root):
        if not root: return 0
        d = map(self.minDepth, (root.left, root.right))
        return 1 + min(d) if min(d)!=0 else 1 + max(d)

# other good solution:
# key: can use map to build link of left and right node with maxDepth

 class Solution(object):
    def minDepth(self, root):
        if not root: return 0
        d, D = sorted(map(self.minDepth, (root.left, root.right)))
        return 1 + (d or D)
