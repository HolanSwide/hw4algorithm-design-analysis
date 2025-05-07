
from graphviz import Digraph

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def delete(root, key):
    if root is None:
        return root
    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = minValueNode(root.right)
        root.val = temp.val
        root.right = delete(root.right, temp.val)
    return root

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def visualize(tree, filename):
    dot = Digraph()
    visualize_helper(tree, dot)
    dot.render(filename, format='png', cleanup=True)

def visualize_helper(node, dot):
    if node:
        dot.node(str(node.val))
        if node.left:
            dot.edge(str(node.val), str(node.left.val))
            visualize_helper(node.left, dot)
        if node.right:
            dot.edge(str(node.val), str(node.right.val))
            visualize_helper(node.right, dot)

# Build initial BST
keys = [48, 33, 49, 47, 42, 46, 32]
root = None
for key in keys:
    root = insert(root, key)
visualize(root, 'fig/hw3_1')

# Delete 33 and visualize
root = delete(root, 33)
visualize(root, 'fig/hw3_2')
