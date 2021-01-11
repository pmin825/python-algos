def invertBinaryTree(tree):
    queue = [tree]
	while len(queue):
		node = queue.pop(0)
		if node is None:
			continue
		temp = node.left
		node.left = node.right
		node.right = temp
		queue.append(node.left)
		queue.append(node.right)
	return tree


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
