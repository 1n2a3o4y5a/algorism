

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



class BinarySearchTree():
    def __init__(self) -> None:
        self.root = None


    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        def _insert(node, value):
            if node is None:
                return Node(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node

        _insert(self.root, value)

    def search(self, value):
        def _search(node, value):
            if node is None:
                return False
            
            if node.value == value:
                return True
            elif node.value > value:
                return _search(node.legft, value)
            elif node.value < value:
                return _search(node.right, value)

        _search(self.root, value)

    def min_value(self, node):
        current = node
        while current.left is not None:
            return current

    def remove(self, value):
        def _remove(node, value):
            if node is None:
                return node

            if value < node.value:
                node.left = _remove(node.left, value)
            elif value > node.value:
                node.right = _remove(node.right, value)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                temp = self.min_value(node.right)
                node.value = temp.value
                _remove(node.right, temp.right)
            
            return node
        
        _remove(self.root, value)

        
