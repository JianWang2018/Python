# Given two binary trees, write a function to check if they are equal or not.
#
# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

# key: if both p and q exists, check if p.value == q.value, p.left == q.left and p.right==q.right, otherwise
# p and q should all be None
import time
class Solution(object):
    def isSameTree(self, p, q):
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p == q==None




# other good solution:

#The "tupleify" way:

def isSameTree(self, p, q):
    def t(n):
        return n and (n.val, t(n.left), t(n.right))
    return t(p) == t(q)
#The first way as one-liner:

def isSameTree(self, p, q):
    return p and q and p.val == q.val and all(map(self.isSameTree, (p.left, p.right), (q.left, q.right))) or p is q