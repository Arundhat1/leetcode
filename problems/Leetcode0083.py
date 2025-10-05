# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Remove duplicates from a sorted linked list.
      
        Args:
            head: The head node of a sorted linked list
          
        Returns:
            The head of the linked list with duplicates removed
        """
        # Initialize current pointer to traverse the list
        current = head
      
        # Traverse the list until we reach the end
        while current and current.next:
            # Check if current node's value equals the next node's value
            if current.val == current.next.val:
                # Skip the duplicate node by updating the pointer
                current.next = current.next.next
            else:
                # Move to the next node if no duplicate found
                current = current.next
      
        # Return the modified list
        return head
