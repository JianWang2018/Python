# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# key: return depth and balance together

import time
class Solution(object):
    def depthAndBalan(self, root):
        if root is None:
            return 1, True
        leftDep, leftBal = self.depthAndBalan(root.left)
        rightDep, rightBal = self.depthAndBalan(root.right)
        curBal = abs(leftDep - rightDep) <= 1
        return max(leftDep, rightDep)+1, leftBal and rightBal and curBal

    def isBalanced(self, root):
        return self.depthAndBalan(root)[1]

# other good solution:
# key: can use map to build link of left and right node with maxDepth

 class Solution(object):
    def isBalanced(self, root):

        def check(root):
            if root is None:
                return 0
            left  = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return check(root) != -1

class Solution(object):
    def isBalanced(self, root):
        stack, node, last, depths = [], root, None, {}
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    node = stack.pop()
                    left, right  = depths.get(node.left, 0), depths.get(node.right, 0)
                    if abs(left - right) > 1: return False
                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right
        return True