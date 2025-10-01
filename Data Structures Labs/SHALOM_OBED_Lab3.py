  
class TwoStack:
    def __init__(self, n):
        self.size = n #capacity
        self.arr = [None] * n
        self.top_left = -1  # top of left stack
        self.top_right = n  # top of right stack
    
    def push_left(self, item):
        if self.top_left < self.top_right - 1:
            self.top_left += 1
            self.arr[self.top_left] = item
        else:
            raise OverflowError("Stack Overflow")
    
    def push_right(self, item):
        if self.top_left < self.top_right - 1:
            self.top_right -= 1
            self.arr[self.top_right] = item
        else:
            raise OverflowError("Stack Overflow")
    
    def pop_left(self):
        if self.top_left >= 0:
            item = self.arr[self.top_left] 
            self.top_left -= 1
            return item
        else:
            raise IndexError("Stack Underflow")
    
    def pop_right(self):
        if self.top_right < self.size:
            item = self.arr[self.top_right] 
            self.top_right += 1
            return item
        else:
            raise IndexError("Stack Underflow")
    
    def len_left(self):
        return self.top_left + 1
    
    def len_right(self):
        return self.size - self.top_right
    
    def transfer_to_left(self, n):
        if n > self.len_right():
            raise ValueError(f"Can't transfer {n} items. Right stack has only {self.len_right()} items")
        
        for _ in range(n):
            item = self.pop_right()
            self.push_left(item)
    
    def transfer_to_right(self, n):
        if n > self.len_left():
            raise ValueError(f"Can't transfer {n} items. Left stack has only {self.len_left()} items")

        for _ in range(n):
            item = self.pop_left()
            self.push_right(item)
    
    def display(self):
        print(f"Array: {self.arr}")
        print(f"Left stack: {self.arr[:self.top_left + 1]}")
        print(f"Right stack: {self.arr[self.top_right:]}")
        print(f"Left stack size: {self.len_left()}, Right stack size: {self.len_right()}")
        print("-" * 50)


# Driver code
if __name__ == "__main__":
    
    # Initialize with capacity of 8
    ts = TwoStack(8)
    print("Initialized TwoStack with capacity 8")
    ts.display()
    
    # Push items to left stack
    ts.push_left(10)
    ts.push_left(20)
    ts.push_left(30)
    ts.display()
    
    # Push items to right stack
    ts.push_right('A')
    ts.push_right('B')
    ts.push_right('C')
    ts.display()
    
    # Pop from both stacks
    print("Popping from left stack:")
    popped_left = ts.pop_left()
    ts.display()
    
    print("Popping from right stack:")
    popped_right = ts.pop_right()
    ts.display()
    
    # Check lengths
    print(f"Left stack length: {ts.len_left()}")
    print(f"Right stack length: {ts.len_right()}")
    print()
    
    # Transfer operations
    print("Transferring item from right stack to left stack:")
    ts.transfer_to_left(1)
    ts.display()
    
    print("Transferring 2 items from left stack to right stack:")
    ts.transfer_to_right(2)
    ts.display()
