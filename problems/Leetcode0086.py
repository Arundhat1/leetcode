# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#strategy - reverse the list from left-node to right-node considering that 
# is independent list and then merging it into original list
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        def reverse(headnode:Optional[ListNode],reverse_nodes:int)-> Optional[ListNode],Optional[ListNode]:
            dummy = ListNode()
            dummy.next = headnode
            prev = dummy
            curr = headnode.next
            i = 0
            while curr and i < reverse_nodes:
                if not  curr.next:
                    curr.next = prev
                    return headnode
                Next_node = curr.next
                curr.next = prev
                curr = Next_node
                i += 1
            return headnode, curr
            

        dummy = ListNode()
        dummy.next = head
        prev = dummy
        i = 0
        temp = head
        while temp:
            if i  + 1 == left:
                prev = temp
            elif i == left:
                left_node = temp
            elif i-1 == right:
                Next = temp
            elif i == right:
                right_node = temp
            temp = temp.next
        new_head, newtail = reverse(left_node,left-right+1)
        prev.next = new_head
        if Next:
            newtail.next = Next 
        return dummy.next


         
        
