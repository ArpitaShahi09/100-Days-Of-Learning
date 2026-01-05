# --- Day 2: Professional Linked List Implementation ---

class Node:
    """A Lead-Coder approach to defining data structures."""
    def __init__(self, value):
        self.value = value
        self.next = None

# Creating a small chain (List)
head = Node("Start")
head.next = Node("Middle")
head.next.next = Node("End")

print("✨ Linked List Chain created successfully!")
