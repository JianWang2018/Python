# Reverse a singly linked list.
#
# click to show more hints.
#
# Hint:
# A linked list can be reversed either iteratively or recursively. Could you implement both?


# key: can change the direction when loop in each node

import time

# iterative
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev=None
        while head:
            temp=head
            head=head.next
            temp.next=prev
            prev=temp
        return prev


# recursive

class Solution:
# @param {ListNode} head
# @return {ListNode}
    def reverseList(self, head):
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)

# other solution
#key: can use set to store past value

