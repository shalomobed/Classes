# Node class
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

#Function to insert a value into the list 
def sortedInsert(head, data):
    new_node = Node(data)
    
    if head is None:
        new_node.next = new_node
        return new_node

    curr = head

    while True:
        if curr.data <= data <= curr.next.data:
            new_node.next = curr.next
            curr.next = new_node
            return head
        
        if data > curr.next.data:
            if data <= curr.next.data or data >= curr.data:
                new_node.next = curr.next
                curr.next = new_node
                return head
        
        curr = curr.next
        if curr == head:
            break
        


    new_node.next = curr.next
    curr.next = new_node
    return head

#Driver code
if __name__ == "__main__":
    #head = [3, 4, 1]
    head = Node(3)
    head.next = Node(4)
    head.next.next = Node(1)
    head.next.next.next = head #Making it circular by connecting the tail to the head

    #insertVal = 2
    head = sortedInsert(head, 2)

    #Print circular list starting with the head
    curr = head
    if head is not None:
        while True:
            print(curr.data, end=" ") #Print the current node's data
            curr = curr.next #Move to the next node
            if curr == head: #Stop when the circle is complete
                break
    print()