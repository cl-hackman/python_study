# first watch how to create a linked list on yotube : https://www.youtube.com/watch?v=JlMyYuY1aXU&list=LL&index=39&t=303s
# Add in reverse order
''' create a head node
    create a pointer
    create a counter (to accomodate for carrying when adding)
    if the linked lists have values in them, extract them to v1 & v2
    add up these values 
    update the pointer 
    update the carry '''


class ListNode:
    # every node in a linked list consists of data and a pointer unless the last node
    def __init__(self, val=0, next=None):
        self.val = val  # (data)
        self.next = next  # (pointer)


class Solution:

    def addlinkedlists(self, l1, l2):
        # reversing the lists
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        head = None
        carry = 0
        while l1 or l2:  # this says: while we're in the nodes and not in the null part of the linked list
            # get the current values
            x1 = l1.val if l1 else 0
            x2 = l2.val if l2 else 0

            # current sum and carry
            val = (carry + x1 + x2) % 10    #to get the remainder
            carry = (carry + x1 + x2) // 10 #to let python know that this carry is the remainder since we get no remainder with //

            # create head node and pointer reverse the result
            curr = ListNode(val)
            curr.next = head
            head = curr

            # move to the next elements in the lists when there's nothing there then NONE
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            # if there's carry with the first addition, then the head node will have the remainder carry as the pointer
        if carry:
            curr = ListNode(carry)
            curr.next = head
            head = curr

        return head
