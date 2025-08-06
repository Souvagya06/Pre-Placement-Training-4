
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class Solution:
    def sortedInsert(self, head, x):
        new_node = Node(x)
        #for empty list
        if head is None:
            return new_node
        #for insertion before head
        if x<head.data:
            new_node.next = head
            head.prev = new_node
            return new_node
        #insertion after the head (somewhere)
        curr = head
        while curr.next and curr.next.data<x:
            curr = curr.next
        new_node.next = curr.next
        if curr.next:
            curr.next.prev =new_node
        curr.next = new_node
        new_node.prev = curr
        return head
