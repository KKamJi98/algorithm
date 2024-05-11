class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList(object):
  def __init__(self):
    self.head = None
    self.tail = None

  def append(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
    else:
      current = self.head
      while current.next:
        current = current.next
      current.next = new_node
    self.tail = new_node

  def get(self, idx):
    cur = self.head
    cur_idx = 0
    while cur_idx != idx:
      if cur.next == None:
        return None
      cur_idx += 1
      cur = cur.next
    return cur.data

  def get_node(self, idx):
    cur = self.head
    cur_idx = 0
    while cur_idx != idx:
      if cur.next == None:
        print("index out of range")
        return
      cur_idx += 1
      cur = cur.next
    return cur

  def insert_at(self, idx, value):
    if idx == 0:
      tmp_node = self.head
      self.head = Node(value)
      self.head.next = tmp_node
      return
    else:
      cur_idx = 0
      cur = self.head
      while cur_idx != idx - 1:
        if cur.next == None:
          print("index out of range")
          return
        cur_idx += 1
        cur = cur.next
      new_node = Node(value)
      new_node.next = cur.next
      cur.next = new_node

  def remove_at(self, idx):
    if idx == 0:
      self.head = self.head.next
    else:
      cur_node = self.get_node(idx-1)
      if cur_node.next == None:
        print("index out of range")
        return
      cur_node.next = cur_node.next.next

  def insert_back(self, value):  # O(1) tail need
    if self.head is None:
      self.head = Node(value)
      self.tail = self.head
    else:
      self.tail.next = Node(value)
      self.tail = self.tail.next


ll = LinkedList()
ll.insert_back(9)
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.insert_at(0, 0)
ll.remove_at(5)
ll.insert_back(8)
ll.insert_back(7)

# 출력
cur = ll.head
while True:
  print(cur.data)
  if not cur.next:
    break
  cur = cur.next

idx = 0
if ll.get_node(idx):
  print(f"idx => {idx} \t data => {ll.get_node(idx).data}")
