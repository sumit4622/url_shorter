class Node:
    def __init__(self, key, value):
        self.key = key          # Stores the Long URL string
        self.value = value      # Stores the Short Code string
        self.prev = None        # Pointer to the previous Node object
        self.next = None        # Pointer to the next Node object
        
    # Getters and Setters for Value (Data)
    def get_value(self):
        return self.value
    
    def set_value(self, new_value):
        self.value = new_value

    # Getters and Setters for Next Pointer
    def get_next(self):
        return self.next
        
    def set_next(self, new_next):
        self.next = new_next

    # Getters and Setters for Prev Pointer (Crucial for Doubly Linked Lists!)
    def get_prev(self):
        return self.prev
        
    def set_prev(self, new_prev):
        self.prev = new_prev