# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        temp = head
        prev = dummy
        prev_initiated = False

        # move temp1 ahead by n steps
        temp1 = head
        for _ in range(n):
            temp1 = temp1.next

        # move temp and temp1 together until temp1 reaches the end
        while temp1:
            temp1 = temp1.next
            prev = temp
            temp = temp.next
            if not prev_initiated:
                prev_initiated = True

        # delete the nth node
        prev.next = temp.next
        temp.next = None

        return dummy.next
