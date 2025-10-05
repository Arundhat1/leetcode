class Node:
    """
    Represents a node in the doubly-linked list.
    Each node stores a count value and all keys that have that count.
    """
    def __init__(self, key: str = '', count: int = 0):
        self.prev = None  # Previous node in the linked list
        self.next = None  # Next node in the linked list
        self.count = count  # The count value this node represents
        self.keys = {key} if key else set()  # Set of keys with this count
  
    def insert_after(self, new_node: 'Node') -> 'Node':
        """
        Insert a new node right after the current node.
        Returns the newly inserted node.
        """
        new_node.prev = self
        new_node.next = self.next
        self.next.prev = new_node
        self.next = new_node
        return new_node
  
    def remove(self) -> None:
        """
        Remove this node from the linked list by connecting 
        its previous and next nodes directly.
        """
        self.prev.next = self.next
        self.next.prev = self.prev


class AllOne:
    """
    A data structure that maintains string keys with their counts.
    Supports incrementing/decrementing counts and retrieving keys with min/max counts.
    All operations run in O(1) time.
    """
    def __init__(self):
        # Create a sentinel root node for the circular doubly-linked list
        self.root = Node()
        self.root.next = self.root
        self.root.prev = self.root
      
        # Map each key to its corresponding node in the linked list
        self.key_to_node = {}
  
    def inc(self, key: str) -> None:
        """
        Increment the count of the given key by 1.
        If the key doesn't exist, initialize it with count 1.
        """
        if key not in self.key_to_node:
            # Key doesn't exist, need to add it with count 1
            if self.root.next == self.root or self.root.next.count > 1:
                # No node with count 1 exists, create a new one
                new_node = Node(key, 1)
                self.key_to_node[key] = self.root.insert_after(new_node)
            else:
                # Node with count 1 already exists, add key to it
                self.root.next.keys.add(key)
                self.key_to_node[key] = self.root.next
        else:
            # Key exists, increment its count
            current_node = self.key_to_node[key]
            next_node = current_node.next
            new_count = current_node.count + 1
          
            # Check if we need to create a new node for the incremented count
            if next_node == self.root or next_node.count > new_count:
                # Create new node with incremented count
                new_node = Node(key, new_count)
                self.key_to_node[key] = current_node.insert_after(new_node)
            else:
                # Node with the target count already exists
                next_node.keys.add(key)
                self.key_to_node[key] = next_node
          
            # Remove key from current node
            current_node.keys.discard(key)
            if not current_node.keys:
                # If node has no keys left, remove it from the list
                current_node.remove()
  
    def dec(self, key: str) -> None:
        """
        Decrement the count of the given key by 1.
        If the count reaches 0, remove the key entirely.
        Assumes the key exists in the data structure.
        """
        current_node = self.key_to_node[key]
      
        if current_node.count == 1:
            # Count will become 0, remove the key entirely
            del self.key_to_node[key]
        else:
            # Decrement the count
            prev_node = current_node.prev
            new_count = current_node.count - 1
          
            # Check if we need to create a new node for the decremented count
            if prev_node == self.root or prev_node.count < new_count:
                # Create new node with decremented count
                new_node = Node(key, new_count)
                self.key_to_node[key] = prev_node.insert_after(new_node)
            else:
                # Node with the target count already exists
                prev_node.keys.add(key)
                self.key_to_node[key] = prev_node
      
        # Remove key from current node
        current_node.keys.discard(key)
        if not current_node.keys:
            # If node has no keys left, remove it from the list
            current_node.remove()
  
    def getMaxKey(self) -> str:
        """
        Return a key with the maximum count.
        If multiple keys have the maximum count, return any one of them.
        Returns empty string if no keys exist.
        """
        if self.root.prev == self.root:
            return ""
        # The last node (root.prev) contains keys with maximum count
        return next(iter(self.root.prev.keys))
  
    def getMinKey(self) -> str:
        """
        Return a key with the minimum count.
        If multiple keys have the minimum count, return any one of them.
        Returns empty string if no keys exist.
        """
        if self.root.next == self.root:
            return ""
        # The first node (root.next) contains keys with minimum count
        return next(iter(self.root.next.keys))




# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
