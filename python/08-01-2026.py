"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:
"""
class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


tree = Node(0, 1, Node(0, Node(1, 1, 1), 0))


def universal_value(node):
    i = 0
    if type(node.left) is Node:
        i += universal_value(node.left)
    if type(node.right) is Node:
        i += universal_value(node.right)
    if node.value == node.left and node.value == node.right:
        i += 1
    if type(node.right) is int:
        i += 1
    if type(node.left) is int:
        i += 1
    return i
