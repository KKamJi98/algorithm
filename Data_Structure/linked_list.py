class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

cur = ll.head
while cur.next:
    print(cur.data)
    cur = cur.next