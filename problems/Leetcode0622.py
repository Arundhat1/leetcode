class ListNode:
    def __init__(self, value=0, nex=None):
        self.val = value
        self.next = nex

class MyCircularQueue:
    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        
        newNode = ListNode(value)
        if self.size == 0:
            self.head = self.tail = newNode
            self.tail.next = self.head  # circular link
        else:
            newNode.next = self.head
            self.tail.next = newNode
            self.tail = newNode
        
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        
        if self.size == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.head.val

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
