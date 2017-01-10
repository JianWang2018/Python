# Invert a binary tree.
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# to
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
# Trivia:
# This problem was inspired by this original tweet by Max Howell:
# Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.
# key: use recursive to revert the noed from bottom to top.

import time
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root



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