# W8_Task:8- 
# Ques:58. K-th Smallest Element in a BST

def kth_smallest(root, k):
    def inorder(node):
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)

    return inorder(root)[k-1]
