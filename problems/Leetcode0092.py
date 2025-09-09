# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right or not head:
            return head

        dummy = ListNode(0)
        dummy.next = head
        i = 1                      # 1-based indexing
        temp = head
        before_left = None
        left_node = None
        after_right = None

        while temp:
            if i == left - 1:
                before_left = temp
            elif i == left:
                left_node = temp
            elif i == right + 1:
                after_right = temp
            temp = temp.next
            i += 1

        # reverse the sublist
        prev = after_right
        curr = left_node
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # reconnect
        if before_left:
            before_left.next = prev
        else:
            dummy.next = prev

        return dummy.next
