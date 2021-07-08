

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

def min_value(node):
    current = node
    while current.left is not None:
        return current

def remove(node, value):
    if node is None:
        return node

    if value < node.value:
        node.left = remove(node.left, value)
    elif value > node.value:
        node.right = remove(node.right, value)
    else:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left

        temp = min_value(node.right)
        node.value = temp.value
        remove(node.right, temp.right)
    
    return node
        

test = None
test = insert(test, 1)
test = insert(test, 2)
test = insert(test, 3)
test = remove(test, 3)