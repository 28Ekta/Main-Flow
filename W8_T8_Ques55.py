# W8_Task:8 -
# Ques:55. Serialize and Deserialize Binary Tree

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string using preorder traversal."""
        def dfs(node):
            if not node:
                return "None,"
            return str(node.val) + "," + dfs(node.left) + dfs(node.right)
        return dfs(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        values = iter(data.split(","))
        def dfs():
            val = next(values)
            if val == "None":
                return None
            node = Node(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

# ---------------- Example Run ----------------
def print_tree(root, level=0, prefix="Root:"):
    """Pretty print the binary tree"""
    if root:
        print("   " * level + prefix + str(root.val))
        print_tree(root.left, level + 1, "L---")
        print_tree(root.right, level + 1, "R---")

if __name__ == "__main__":
    # Build a sample binary tree:
    #        1
    #       / \
    #      2   3
    #         / \
    #        4   5
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(5)

    codec = Codec()

    # Serialize tree
    serialized = codec.serialize(root)
    print("Serialized Tree:")
    print(serialized)

    # Deserialize back to tree
    deserialized_root = codec.deserialize(serialized)

    print("\nDeserialized Tree Structure:")
    print_tree(deserialized_root)








