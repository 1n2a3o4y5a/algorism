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
        new_node.previous = current_node
    
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        self.head.previous = new_node
        new_node.next = self.head
        self.head = new_node
    
    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
    
    def remove(self, data):
        current_node = self.head
        if current_node and current_node.data == data:
            if current_node.next is None:
                current_node = None
                self.head = None
                return
            else:
                next_node = current_node.next
                next_node.previous = None
                current_node = None
                self.head = next_node
                return
        
        while current_node and current_node.data != data:
            current_node = current_node.next
        
        if current_node is None:
            return
        
        if current_node.next is None:
            previous = current_node.previous
            previous.next = None
            current_node = None
            return
        else:
            next_node = current_node.next
            previous_node = current_node.previous
            previous_node.next = next_node
            next_node.previous = previous_node
            current_node = None
            return
    
    def reverse_iterate(self):
        previous_node = None
        current_node = self.head

        while current_node:
            previous_node = current_node.previous
            current_node.previous = current_node.next
            current_node.next = previous_node

            current_node = current_node.previous
        
        if previous_node:
            self.head = previous_node.previous
    
    def reverse_recursive(self):
        def inner_recursive(current_node):
            if not current_node:
                return None

            previous_node = current_node.previous
            current_node.previous = current_node.next
            current_node.next = previous_node

            if current_node.previous is None:
                return current_node
        
            return inner_recursive(current_node.previous)
        
        self.head = inner_recursive(self.head)

li = DoubleLinkedList()
li.appned(1)
li.appned(2)
li.appned(3)
li.insert(0)
li.appned(4)
li.appned(5)
li.print()
print(11111111111111)
li.remove(2)
li.print()
