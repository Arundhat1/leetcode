class MinStack:
    def __init__(self):
        self.stack = []
        self.min_val = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.min_val = val
        elif val >= self.min_val:
            self.stack.append(val)
        else:  # val < min_val → encode
            encoded_val = 2 * val - self.min_val
            self.stack.append(encoded_val)
            self.min_val = val

    def pop(self) -> int:
        top = self.stack.pop()
        if top >= self.min_val:
            return top
        else:  # encoded value
            original_min = self.min_val
            self.min_val = 2 * self.min_val - top  # recover previous min
            return original_min

    def top(self) -> int:
        top = self.stack[-1]
        if top >= self.min_val:
            return top
        else:  # encoded, so real top is min_val
            return self.min_val

    def getMin(self) -> int:
        return self.min_val
