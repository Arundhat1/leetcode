# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):
        
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
    
    # Step 2: push first half
        stack = []
        temp = head
        for _ in range(n // 2):
            stack.append(temp.val)
            temp = temp.next
    
    # Step 3: skip middle if odd
        if n % 2 == 1:
            temp = temp.next
    
    # Step 4: compare
        while temp:
            if stack.pop() != temp.val:
                return False
            temp = temp.next
    
        return True
