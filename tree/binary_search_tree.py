

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None




def insert(node, value):
    if node is None:
        return Node(value)
    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node

def search(node, value):
    if node is None:
        return False
    
    if node.value == value:
        return True
    elif node.value > value:
        return search(node.legft, value)
    elif node.value < value:
        return search(node.right, value)