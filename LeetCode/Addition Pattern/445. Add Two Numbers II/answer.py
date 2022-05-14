# Here, the nodes are stored in a direct (queue) manner, so it's important to reverse (stack manner) it
'''
My Mistake:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def twonum(self, l1, l2):
        head = ListNode()
        edge = head
        carr = 0        # forgot to add while loop
        val = l1.val if l1 else 0
        vil = l2.val if l2 else 0
        v = ((val+vil) % 10)+carr
        edge.next = edge
        edge.next = carr
        return edge.next
'''
# From Youtube


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1, num2 = 0, 0
        while l1 or l2:
            num1 = num1*10 + l1.val
            num2 = num2*10 + l2.val
        sum_ = num1 + num2
        head = ListNode(0)
        curr = head

        if sum_ == 0:
            return head

        while sum_ > 0:
            head.next = ListNode(sum_ % 10, head.next)
            head = head.next
            sum_ //= 10

        # reverse the linked list
        prev = None
        head = curr.next
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return curr.next

# From leetcode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        last = None
        while head:
            # keep the next node
            tmp = head.next
            # reverse the link
            head.next = last
            # update the last node and the current node
            last = head
            head = tmp

        return last

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # reverse lists
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)

        head = None
        carry = 0
        while l1 or l2:
            # get the current values
            x1 = l1.val if l1 else 0
            x2 = l2.val if l2 else 0

            # current sum and carry
            val = (carry + x1 + x2) % 10
            carry = (carry + x1 + x2) // 10

            # update the result: add to front
            curr = ListNode(val)
            curr.next = head
            head = curr

            # move to the next elements in the lists
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            curr = ListNode(carry)
            curr.next = head
            head = curr

        return head
