from collections import deque


class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, cur_node, key):
        if key < cur_node.val:
            if cur_node.left is None:
                cur_node.left = Node(key)
            else:
                self._insert(cur_node.left, key)
        else:
            if cur_node.right is None:
                cur_node.right = Node(key)
            else:
                self._insert(cur_node.right, key)

    def preorder(self, root):
        if root:
            print(root.val, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=" ")
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val, end=" ")

    def bfs(self):
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            print(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def height(self, root):
        if root is None:
            return -1
        else:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
        return max(left_height, right_height) + 1


obj = BinaryTree()
obj.insert(8)
obj.insert(9)
obj.insert(7)
obj.insert(6)
obj.insert(5)
obj.insert(4)
obj.preorder(obj.root)
print("-------------------")
obj.inorder(obj.root)
print("-------------------")
obj.postorder(obj.root)
print("-------------------")
obj.bfs()
print("-------------------")
height = obj.height(obj.root)
print("height", height)
