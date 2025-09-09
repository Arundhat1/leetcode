class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        # only enter loop if there are AT LEAST two nodes to swap
        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            # swap
            first.next = second.next
            second.next = first
            prev.next = second

            # move prev forward by 2 (since 'first' is now after 'second')
            prev = first

        return dummy.next
