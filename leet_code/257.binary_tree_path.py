# Given a binary tree, return all root-to-leaf paths.
#
# For example, given the following binary tree:
#
#    1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:
#
# ["1->2->5", "1->3"]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# key: use recursive method
class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        self.dfs(root, "", res)
        return res

    def dfs(self, root, ls, res):
        if not root.left and not root.right: # both are none, it is a leaf return
            res.append(ls+str(root.val))
        if root.left: # left node is not none, then go to the left node
            self.dfs(root.left, ls+str(root.val)+"->", res)
        if root.right:# right node is not none, then go to the right node
            self.dfs(root.right, ls+str(root.val)+"->", res)





# other solution
# key:can use sorted
# dfs + stack
def binaryTreePaths1(self, root):
    if not root:
        return []
    res, stack = [], [(root, "")]
    while stack:
        node, ls = stack.pop()
        if not node.left and not node.right:
            res.append(ls+str(node.val))
        if node.right:
            stack.append((node.right, ls+str(node.val)+"->"))
        if node.left:
            stack.append((node.left, ls+str(node.val)+"->"))
    return res

# bfs + queue
def binaryTreePaths2(self, root):
    if not root:
        return []
    res, queue = [], collections.deque([(root, "")])
    while queue:
        node, ls = queue.popleft()
        if not node.left and not node.right:
            res.append(ls+str(node.val))
        if node.left:
            queue.append((node.left, ls+str(node.val)+"->"))
        if node.right:
            queue.append((node.right, ls+str(node.val)+"->"))
    return res

# five lines code
def binaryTreePaths(self, root):
    if not root:
        return []
    if not root.left and not root.right:
            return [str(root.val)]
    return [str(root.val)+"->" + i for sub in (root.left, root.right)
            for i in self.binaryTreePaths(sub) if sub]

import time

def main():
    a="asaba"
    b="abasa"
    time_t=time.time()
    sln=Solution().isAnagram(a,b)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()