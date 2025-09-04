"""
A simple Queue implementation in Python (FIFO - First In, First Out).

Features:
- put(): add element to the queue
- get(): remove and return element from the queue
- isempty(): check if the queue is empty

Example:
    que = Queue()
    que.put(1)
    que.put("dog")
    print(que.get())  # Output: 1
"""

class Queue:
    def __init__(self):
        # Create an empty list to store elements
        self._queue = []  
    
    def put(self, elem):
        """Add element to the queue (FIFO)."""
        # Insert new element at the beginning of the list
        self._queue.insert(0, elem)
    
    def get(self):
        """Remove and return the next element in the queue.
        Raises IndexError if the queue is empty."""
        # Take and remove the last element in the list
        return self._queue.pop()  
    
    def isempty(self):
        """Return True if the queue is empty, otherwise False."""
        # Check if list is empty
        return not self._queue  
        

# Example usage
que = Queue()
que.put(1)        # Add number
que.put("dog")    # Add string
que.put(False)    # Add boolean

for i in range(4):  # Try to get 4 elements
    if not que.isempty():
        print(que.get())  # Print element from queue
    else:
        print("Queue empty")  # Queue is empty
