class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_position(self, pos, data):
        new_node = Node(data)
        if pos <= 0:
            print("Invalid position")
            return
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        for _ in range(pos - 2):
            if not temp:
                print("Position out of range")
                return
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def delete_at_beginning(self):
        if not self.head:
            print("List is empty")
            return
        self.head = self.head.next

    def delete_at_end(self):
        if not self.head:
            print("List is empty")
            return
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


print("📘 Singly Linked List Operations:\n")
sll = SinglyLinkedList()


sll.insert_at_beginning(10)
sll.insert_at_beginning(5)
print("After inserting 5 and 10 at beginning:")
sll.display()


sll.insert_at_end(20)
print("After inserting 20 at end:")
sll.display()


sll.insert_at_position(2, 15)
print("After inserting 15 at position 2:")
sll.display()


sll.delete_at_beginning()
print("After deleting at beginning:")
sll.display()


sll.delete_at_end()
print("After deleting at end:")
sll.display()

