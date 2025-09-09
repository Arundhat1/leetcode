# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = head
        if not head:
            return head
        temp1 = head
        if not temp1.next:
            return head
        temp2 = temp1.next
        while temp1:
            if temp1.val == temp2.val:
                while temp2.next.val == temp1.val:
                    temp2 = temp2.next
                if not temp2.next:
                    prev.next = None
                    return head
                Next = temp2.next
                prev.next = Next
                temp2.next = None
                temp1 = Next
                if not temp1.next:
                    return head
                temp2 = temp1.next
            else:
                prev = prev.next
                temp1 = temp1.next
                if not temp2.next:
                    return head
                temp2 = temp2.next
            
        
