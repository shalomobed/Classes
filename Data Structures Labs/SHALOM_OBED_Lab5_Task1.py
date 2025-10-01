class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
#TASK 1
def concatenate(h1, h2):
    #Concatenates the linked lists
    if h1 is None:
        return h2
        
    curr = h1
    while curr.next is not None:
        curr = curr.next
        
    curr.next = h2
    
    return h1

def get_length(head):
    #finds the length of the linked lists
    count = 0
    curr = head
    while curr is not None:
        count += 1
        curr = curr.next
    return count

def printList(head):
    #Outputs the list
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()
    
if __name__ == "__main__":
    #CASE #1
    #Create first linked list
    h1 = Node(3)
    h1.next = Node(4)
    h1.next.next = Node(5)
    
    #Create second linked list
    h2 = Node(1)
    h2.next = Node(2)

    #Calculates the shorter linked list
    len1 = get_length(h1)
    len2 = get_length(h2)

    if len1 < len2:
        result = concatenate(h1, h2)
    else:
        result = concatenate(h2, h1)
    print("Case #1")
    printList(result)

    #CASE #2
    #Create first linked list
    h3 = Node(4)
    h3.next = Node(5)

    #Create second linked list
    h4 = Node(1)
    h4.next = Node(2)
    h4.next.next = Node(3)

    #Calculates the shorter linked list
    len3 = get_length(h3)
    len4 = get_length(h4)
    
    if len3 < len4:
        result2 = concatenate(h3, h4)
    else:
        result2 = concatenate(h4, h3)
    print("\nCase #2")
    printList(result2)


























