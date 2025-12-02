class Node:
    def __init__(self, d):
        self.data = d
        self.right = None # traverses to the right 
        self.left = None # traverses to the left

#Calculating the height of a tree
def height(node):
    if node is None:
        return 0
    
    lheight_node = height(node.left) # left height
    rheight_node = height(node.right) # right height

    #return 1 + maximum between left height and right height
    return 1 + max(lheight_node, rheight_node)

#Checking if the tree is balanced
def is_balanced(root):
    if root is None:
        return True

    lheight_root = height(root.left) # height of left subtree
    rheight_root = height(root.right) # height of right subtree

    if abs(lheight_root - rheight_root) > 1: # if the difference between the left and right subtree is greater than 1...
        return False # the tree is unbalanced
    
    #recursively checking...
    return is_balanced(root.left) and is_balanced(root.right)

#Checking if it is a Binary Search
def is_BST_util(node, min_val, max_val):
    if node is None:
        return True
    
    if node.data < min_val or node.data > max_val:
        return False
    
    return (is_BST_util(node.left, min_val, node.data - 1) and is_BST_util(node.right, node.data + 1, max_val))

def is_BST(root):
    return is_BST_util(root, float('-inf'), float('inf'))

#FUNCTION TO CHECK IF IT IS AN AVL TREE
def is_valid_AVL_tree(root):
    return is_balanced(root) and is_BST(root)

if __name__ == "__main__":
    print("A Valid AVL Tree")
    root1 = Node(3)
    root1.left = Node(1)
    root1.right = Node(5)
    root1.right.left = Node(4)
    root1.right.right = Node(8)
    print(is_valid_AVL_tree(root1))

    print("\nInvalid AVL Tree (balanced, but not a BST)")
    root2 = Node(3)
    root2.left = Node(1)
    root2.right = Node(5)
    root2.right.left = Node(4)
    root2.right.right = Node(2)
    print(is_valid_AVL_tree(root2))

    print("\nInvalid AVL Tree (a BST, but not balanced)")
    root3 = Node(3)
    root3.left = Node(1)
    root3.right = Node(5)
    root3.right.left = Node(4)
    root3.right.right = Node(8)
    root3.right.right.right = Node(9)
    print(is_valid_AVL_tree(root3))
