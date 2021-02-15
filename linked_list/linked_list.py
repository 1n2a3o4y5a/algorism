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
            current_node = None
            return

        previous_node = None
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            return

        previous_node.next = current_node.next
        current_node = None


    def reverse_iterate(self):
        porevious_node = None
        current_node = self.head

        while current_node:
            next_node = current_node.next
            current_node.next = next_node
            porevious_node = current_node
            current_node = next_node
        
        self.head = porevious_node

    def reverse_recursive(self):
        def inner_recursive(current_node, previous_node):
            if not current_node:
                return previous_node
            
            next_node = current_node.next
            current_node.next = next_node
            previous_node = current_node
            current_node = next_node
            return inner_recursive(current_node, previous_node)
        
        self.head = inner_recursive(self.head, None)
    
    def reverse_even(self):

        def inner_even(head, previous_node):
            if head is None:
                return None
            current_node = head
            while current_node and current_node % 2 == 0:
                next_node = current_node.next
                current_node.next = next_node
                previous_node = current_node
                current_node = next_node

            if current_node != head:
                head.next = current_node
                inner_even(current_node, None)
                return current_node
            else:
                head.next = inner_even(head.next, head):
                return head
            
        self.head = inner_even(self.head, None)






li = LinkedList()
li.appned(1)
li.appned(2)
li.insert(0)
li.appned(3)

li.print()
print(1111111111111111)
li.print()

li.reverse_iterate()