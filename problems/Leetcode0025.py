class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Helper to reverse k nodes starting at head
        def reverse_k_nodes(start, k):
            prev = None
            curr = start
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            # prev = new head of this reversed block
            # start = new tail of this reversed block
            # curr = node after the block
            return prev, start, curr

        # Count total length
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        dummy = ListNode(0, head)
        prev_group_tail = dummy
        curr = head

        # Process in blocks of k
        while length >= k:
            new_head, new_tail, next_start = reverse_k_nodes(curr, k)
            prev_group_tail.next = new_head
            new_tail.next = next_start
            prev_group_tail = new_tail
            curr = next_start
            length -= k

        return dummy.next

        
