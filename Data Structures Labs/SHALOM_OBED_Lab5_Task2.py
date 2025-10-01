class Node: 
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
#TASK 2
def findLength(doublyNode):
    #finding the length
    length = 0
    while doublyNode:
        length += 1
        doublyNode = doublyNode.next
    return length

if __name__ == "__main__":
    #Driver code
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next
    head.next.next.next = Node(4)
    head.next.next.next.prev = head.next.next
    print("\nThe length of doubly linked list:")
    print(findLength(head))