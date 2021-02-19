class Node(object):
    def __init__(self, data, next_node=None, previous_node=None):
        self.data = data
        self.next = next_node
        self.previous = previous_node


class DoubleLinkedList:
    def __init__(self, head=None, Node=None):
        self.head = head
    
    def appned(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node
        current_node.previous = current_node

li = DoubleLinkedList()
li.appned(1)
