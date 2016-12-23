# Given a linked list, remove the nth node from the end of list and return its head.
#
# For example,
#
#    Given linked list: 1->2->3->4->5, and n = 2.
#
#    After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Try to do this in one pass.


# key: use two node, after first node loop n times the second node start to loop
class Solution(object):
    def removeNthFromEnd(self, head, n):
        first = second = head
        for i in range(n):
            first = first.next
        # if the length of list is less than n
        if not first:
            return head.next
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return head


def main():
    print('1')

if __name__=="__main__":
    main()