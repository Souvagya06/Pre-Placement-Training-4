class Solution:
    def delete_node(self, head, x):
        # If DLL is empty
        if not head:
            return None

        # If x=0
        if x == 1:
            next_node = head.next
            if next_node:
                next_node.prev = None
            head = next_node
            return head

        curr = head
        count = 1

        # Traverse to the node to be deleted
        while curr and count < x:
            curr = curr.next
            count += 1

        # If position is more than number of nodes
        if not curr:
            return head

        # Adjust pointers
        if curr.prev:
            curr.prev.next = curr.next
        if curr.next:
            curr.next.prev = curr.prev

        return head
