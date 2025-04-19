class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class InsertNodeAtHead:
    def __init__(self):
        self.head = None
    
    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = Node(data)
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next

            current_node.next = new_node
    
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        
        print("None")
    

ll = InsertNodeAtHead()
ll.print()
ll.add(10)
ll.add(20)
ll.add(30)
ll.add(40)
ll.add(50)

ll.print()

ll.insert_at_head(10101)
ll.print()