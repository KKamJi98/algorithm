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

    def get(self, idx):
        cur = self.head
        cur_idx = 0
        while cur_idx != idx:
            if cur.next == None:
                return None
            cur_idx += 1
            cur = cur.next
        return cur.data
        
    def insert_at(self, idx, value):
        pass
    
    def remove_at(self, idx):
        pass
    
    def insert_back(self, value): # O(1) tail need
        pass

    

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

print(ll.get(0))
print(ll.get(1))
print(ll.get(3))

# print(ll.__sizeof__)

# cur = ll.head
# while cur.next:
#     print(cur.data)
#     cur = cur.next