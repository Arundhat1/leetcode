class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
class Solution:
    def matches(self,open,close):
        opens = "([{"
        closers = ")]}"
        return opens.index(open) == closers.index(close)

    def isValid(self, s: str) -> bool:
        stack = Stack()
        balanced = True
        index = 0
        while index < len(s) and balanced:
            symbol = s[index]
            if symbol in "([{":
                stack.push(symbol)
            else:
                if stack.isEmpty():
                    balanced = False
                else:
                    top = stack.pop()
                    if not self.matches(top,symbol):
                       balanced = False
            index = index + 1
        if balanced and stack.isEmpty():
            return True
        else:
            return False


        
