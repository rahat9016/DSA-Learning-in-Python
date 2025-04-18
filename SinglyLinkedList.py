class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, data):
        # First check is head is none or has data
        # if head is none insert data in the first element
        # if head has data insert the data at end of last node
        new_node = Node(data)
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def print(self):
        current = self.head
        while current:
            print(current.data, end=" ->")
            current = current.next


ll = LinkedList()

ll.add(10)
ll.add(20)
ll.add(30)
ll.add(40)
ll.add(50)

ll.print()
