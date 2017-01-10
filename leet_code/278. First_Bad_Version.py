# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
#
# # You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# key: 1) can use binary search 2) should use l+(r-l)/2 to calculate mid to avoid the overflow
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        r = n-1
        l = 0
        while(l<=r):
            mid = l + (r-l)/2
            if isBadVersion(mid)==False:
                l = mid+1
            else:
                r = mid-1
        return l





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