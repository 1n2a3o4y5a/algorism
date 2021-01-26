class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def appned(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, data):
        new_node = Node(data)
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
            self.head = current_node.next
        previous_node = None
        while current_node and current_node.data != data:
            previous_node = current_node
            previous_node.next = current_node.next
        if current_node is None:
            return
        previous_node.next = current_node.next



li = LinkedList()
li.appned(1)
li.appned(2)
li.insert(0)

li.print()
