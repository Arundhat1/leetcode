"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: create mapping old -> new (nodes with only val)
        mapping = {}
        temp = head
        while temp:
            mapping[temp] = Node(temp.val)
            temp = temp.next

        # Step 2: assign next and random using the mapping
        temp = head
        while temp:
            if temp.next:
                mapping[temp].next = mapping[temp.next]
            if temp.random:
                mapping[temp].random = mapping[temp.random]
            temp = temp.next

        # Return deep copy head
        return mapping[head]
