class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)   # add 0 to avoid uninitialized val
        dummy.next = head

        last_sorted = head
        if not head or not head.next:
            return head

        curr = head.next
        while curr:
            if curr.val >= last_sorted.val:
                last_sorted = last_sorted.next
            else:
                # remove curr
                last_sorted.next = curr.next  

                # find insertion spot
                prev = dummy
                while prev.next and prev.next.val <= curr.val:
                    prev = prev.next

                # insert curr between prev and prev.next
                curr.next = prev.next
                prev.next = curr

            # update curr (always after last_sorted)
            curr = last_sorted.next

        return dummy.next
