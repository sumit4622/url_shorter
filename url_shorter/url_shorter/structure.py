from Node import Node

class DoublyLinkedList:
    def __init__(self):
        # Create dummy boundaries to avoid edge-case None pointer errors
        self.head = Node(None, None)
        self.tail = Node(None, None)
        
        # Point head and tail to each other initially
        self.head.set_next(self.tail)
        self.tail.set_prev(self.head)
        
    def is_empty(self):
        """Returns True if the list contains no data nodes."""
        return self.head.get_next() == self.tail
    
    def add_to_front(self, node):
        """
        Inserts a node right after the dummy head.
        This represents the Most Recently Used (MRU) position.
        """
        first_node = self.head.get_next()
        
        node.set_next(first_node)
        node.set_prev(self.head)
        
        self.head.set_next(node)
        first_node.set_prev(node)
        
    def remove(self, node):
        """
        Removes a specific node from anywhere in the list in O(1) constant time
        by updating its neighbors to bypass it.
        """
        prev_node = node.get_prev()
        next_node = node.get_next()
        
        prev_node.set_next(next_node)
        next_node.set_prev(prev_node)
        
    def remove_from_tail(self):
        """
        Removes and returns the oldest node right before the dummy tail.
        This represents the Least Recently Used (LRU) item to be evicted.
        """
        if self.is_empty():
            return None
            
        lru_node = self.tail.get_prev()
        self.remove(lru_node)
        return lru_node

    def traverse(self):
        """Loops through the list from head to tail and prints the data mappings."""
        current = self.head.get_next()
        print("--- Custom Memory List State (Newest -> Oldest) ---")
        while current != self.tail:
            print(f"[{current.get_key()} -> {current.get_value()}]")
            current = current.get_next()
        print("--------------------------------------------------")
        
    def size(self):
        """Calculates the total number of data nodes currently active in the list."""
        current = self.head.get_next()
        count = 0
        while current != self.tail:
            count += 1
            current = current.get_next()
        return count