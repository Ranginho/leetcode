from collections import deque


class Tree:
    def __init__(self, val, left, right):
        self.value = val
        self.left = left
        self.right = right

    def node_equals(self, node):
        if self.value == node.value and self.left == node.left and self.right == node.right:
            return True
        else:
            return False


node1 = Tree(2, None, None)
node2 = Tree(3, None, None)
node3 = Tree(4, None, node2)
root_node = Tree(1, node1, node3)


def inorder_treversal(root):
    if root:
        inorder_treversal(root.left)
        print(root.value)
        inorder_treversal(root.right)


print('Inorder Treversal:')
inorder_treversal(root_node)


def preorder_treversal(root):
    if root:
        print(root.value)
        inorder_treversal(root.left)
        inorder_treversal(root.right)


print('preorder Treversal:')
preorder_treversal(root_node)


def postorder_treversal(root):
    if root:
        inorder_treversal(root.left)
        inorder_treversal(root.right)
        print(root.value)


print('post order Treversal:')
postorder_treversal(root_node)


def level_order_treversal(root):
    queue = deque([root])
    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            print(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


print('level order Treversal:')
level_order_treversal(root_node)

