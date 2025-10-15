class Node:    
    def __init__(self, value, left=None, right=None):
                self.value = value
                self.left = left
                self.right = right
                
# Construct the parse tree for ((7 + 3) * (5 - 2))
root = Node('*')
root.left = Node('+')
root.right = Node('-')
root.left.left = Node(7)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(2)
                
def evaluate(node):
    #Base case: checking if Node is a leaf
    if node.left is None and node.right is None:
        return float(node.value) 
    #Recursive case: computing the left and right numbers
    left_result = evaluate(node.left)
    right_result = evaluate(node.right)

    #Computing the operators
    if node.value == "+":
        return left_result + right_result
    elif node.value == "-":
        return left_result - right_result
    elif node.value == "*":
        return left_result * right_result
    elif node.value == "/":
        return left_result / right_result
    else:
        raise ValueError(f"Unknown operator: {node.value}")
    
print(evaluate(root))#should print 30.0

                
                            


                
