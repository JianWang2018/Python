# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# key: add the small value of l1 and l2,  finally add the remaining of the non empty list, also need a dummy node  point to
# the head of the merge list

# iteratively
def mergeTwoLists1(self, l1, l2):
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next


def main():
    s=["[","]","(",")","["]
    sln=Solution.isValid(s)
    print(sln)

if __name__=="__main__":
    main()