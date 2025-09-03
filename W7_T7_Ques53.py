# W7_Task:7- 
# Ques:53. Zigzag Level Order Traversal of Binary Tree
from collections import deque
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def zigzag_traversal(root):
    if not root:
        return []
    result, dq, left_to_right = [], deque([root]), True
    while dq:
        level = []
        for _ in range(len(dq)):
            node = dq.popleft()
            level.append(node.val)
            if node.left: dq.append(node.left)
            if node.right: dq.append(node.right)
        if not left_to_right:
            level.reverse()
        result.append(level)
        left_to_right = not left_to_right
    return result
root = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(6)))
print(zigzag_traversal(root))  
