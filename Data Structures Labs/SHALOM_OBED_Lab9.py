class Heap:
    def __init__(self):
        self.items = [] 
    
    def is_empty(self):
        return len(self.items) == 0
    
    def insert(self, value):      
        self.items.append(value)
        self.bubble_up(len(self.items) - 1)
    
    def bubble_up(self, i):
        parent = (i- 1) // 2  # index of the parent node
        
        # ensure heap property is valid
        if i > 0 and self.items[i] < self.items[parent]:
            self.items[i], self.items[parent] = self.items[parent], self.items[i]
            self.bubble_up(parent) # Recursively bubble up from the parent's index

    def remove(self):
        if self.is_empty():
            raise Exception("Heap is empty")
        root = self.items[0]
        self.items[0] = self.items[-1]
        self.items.pop()
        if len(self.items) > 0:
            self.bubble_down(0)
        print(f"Removed element: {root}")
        return root
    
    def bubble_down(self, i):
        l = 2 * i + 1  # Left child index
        r = 2 * i + 2  # Right child index
        
        smallest = i # Assume the smallest is the current index
        
        # Check if the left child exists and is smaller than the current
        if l < len(self.items) and self.items[l] < self.items[smallest]:
            smallest = l
        
        # Check if the right child exists and is smaller than the current smallest
        if r < len(self.items) and self.items[r] < self.items[smallest]:
            smallest = r
        
        # If the smallest is not the current index, swap
        if smallest != i:
            self.items[i], self.items[smallest] = self.items[smallest], self.items[i]
            self.bubble_down(smallest)  # And, recursively bubble down the affected child

    def display(self):
        print(self.items)


heap = Heap()
heap.insert(10)
heap.insert(5)
heap.insert(14)
heap.insert(9)
heap.insert(2)
heap.display()


heap.remove()
heap.display()


