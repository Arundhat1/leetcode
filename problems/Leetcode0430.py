"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child 
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        stack = []
        curr = head

        while curr:
            if curr.child:
                # If there's a next, save it for later
                if curr.next:
                    stack.append(curr.next)

                # Stitch child in place
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None

            # If at end of a chain, connect back to stacked node
            if not curr.next and stack:
                nextNode = stack.pop()
                curr.next = nextNode
                nextNode.prev = curr

            curr = curr.next

        return head
