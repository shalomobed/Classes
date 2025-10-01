# Node class representing a process in the system
class Node:
    def __init__(self, pid, burst_time):
        self.pid = pid  # Process ID
        self.burst_time = burst_time  # Remaining burst time
        self.next = None  # Reference to next process

# Circular Linked List class
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, pid, burst_time):
        #Adds a new process to the circular linked list
        new_node = Node(pid, burst_time)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
    
    def remove(self, node):
        #Removes a process from the circular linked list
        if self.head is None:
            return
        
        if self.head == self.tail and self.head == node:
            self.head = None
            self.tail = None
            return
        
        current = self.head
        while current.next != node:
            current = current.next
        
        if node == self.head:
            current.next = self.head.next
            self.head = self.head.next
            self.tail.next = self.head

        elif node == self.tail:
            current.next = self.head
            self.tail = current

        else:
            current.next = node.next
    
    def display(self):
        #Display all processes and their remaining burst time
        if self.head is None:
            print("No processes in the list.")
            return
        
        current = self.head
        print("\nProcesses in the list:")
        while True:
            print(f"Process {current.pid}: Remaining Burst Time = {current.burst_time}")
            current = current.next
            if current == self.head:
                break
    
    def is_empty(self):
        return self.head is None

# Round Robin Scheduler function
def round_robin_scheduler(processes, quantum_time):
    # Create circular linked list and add all processes
    cll = CircularLinkedList()
    for pid, burst_time in processes:
        cll.append(pid, burst_time)
    
    # Display initial state
    cll.display()
    print(f"\nStarting Round Robin Scheduling:")
    
    total_time = 0 
    current = cll.head  
    
    # Continue until all processes are completed
    while not cll.is_empty():
        print(f"\nTime: {total_time}, Processing PID: {current.pid}")
        
        time_to_run = min(quantum_time, current.burst_time)
        
        current.burst_time -= time_to_run
        total_time += time_to_run
        
        if current.burst_time <= 0:
            print(f"Process {current.pid} completed.")
            next_node = current.next
            cll.remove(current)
            
            if not cll.is_empty():
                current = next_node
        else:
            print(f"Process {current.pid} now has {current.burst_time} units remaining.")
            current = current.next
    
    print(f"\nAll processes completed.")
    print(f"Total time taken: {total_time} units")

# Driver code
if __name__ == "__main__":
    processes1 = [(1, 10), (2, 5), (3, 8)]
    quantum_time1 = 4
    round_robin_scheduler(processes1, quantum_time1)
