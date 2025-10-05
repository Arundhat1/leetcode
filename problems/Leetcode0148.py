# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Sort a linked list using merge sort algorithm.
        Time Complexity: O(n log n)
        Space Complexity: O(log n) due to recursion stack
        """
        # Base case: empty list or single node
        if head is None or head.next is None:
            return head
      
        # Find the middle of the list using two pointers
        # slow moves one step, fast moves two steps
        slow = head
        fast = head.next  # Start fast at head.next to ensure slow stops before middle
      
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
      
        # Split the list into two halves
        first_half = head
        second_half = slow.next
        slow.next = None  # Break the connection between two halves
      
        # Recursively sort both halves
        sorted_first = self.sortList(first_half)
        sorted_second = self.sortList(second_half)
      
        # Merge the two sorted halves
        dummy_head = ListNode()  # Dummy node to simplify merge logic
        current = dummy_head
      
        # Merge nodes in sorted order
        while sorted_first and sorted_second:
            if sorted_first.val <= sorted_second.val:
                current.next = sorted_first
                sorted_first = sorted_first.next
            else:
                current.next = sorted_second
                sorted_second = sorted_second.next
            current = current.next
      
        # Attach remaining nodes (if any)
        current.next = sorted_first or sorted_second
      
        return dummy_head.next
