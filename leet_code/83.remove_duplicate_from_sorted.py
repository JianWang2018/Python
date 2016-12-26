# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import time
class Solution(object):
    def deleteDuplicates(self, head):
        cur = head
        while cur:
            while cur.next and cur.next.val==cur.val:
                    cur.next = cur.next.next     # skip duplicated node
            cur = cur.next     # not duplicate of current node, move to next node
        return head






def main():
    n=5
    time_t=time.time()
    sln=Solution().deleteDuplicates(n)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()