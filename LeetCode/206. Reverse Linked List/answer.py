'''This is a sub-problem for many other linked list questions where in the nodes are not stored in REVERSE ORDER.
'''
# watch this youtube video for explanation: https://youtu.be/xg-o3NcmI-E


class Linkedlist:
    # vall=0 since value takes a number/data, next=None since it's an optional argument
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def reverselist(head):
        previous_node = None
        while head:
            first_node = head  # since while looping (brute forcing), the first item in the list is the head node
            head = head.next    # I am setting it's pointer
            first_node.next = previous_node   # now, I am setting the head/current_node's pointer to the previous_node (NULL)
            previous_node = first_node    # as it loops through the list, I am making moving the previous_node to the first/current_node  
        return previous_node                # the while loop will do this till the end



arr = Linkedlist([1, 2, 3, 4, 5])
arr.reverselist()
