
class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None

class Solution:
    def reverseDLL(self, head):
        #return head of reverse doubly linked list
        if head is None or head.next is None:
            return head

        curr = head
        prev = None

        while curr:
            # Swap next and prev pointers
            curr.prev, curr.next = curr.next, curr.prev
            # Move prev to current node
            prev = curr
            # Move to the next node in original list (which is prev after swap)
            curr = curr.prev

        # prev will be the new head at the end of loop
        return prev
