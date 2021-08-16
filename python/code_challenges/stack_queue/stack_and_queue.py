


class Node:
  def __init__(self , value=None):

    self.value= value
    self.next=None

class Stack:
  def __init__(self,node=None):
    self.top=node

  def push(self, value):
    node= Node(value)
    node.next = self.top
    self.top = node

  def pop(self):

    temp=self.top
    self.top=self.top.next
    temp.next=None
    return temp.value

  def is_empty(self):
    return not self.top

  def peek(self):
      if self.top is None:
        raise Exception("its empty")
      return self.top.value


class Queue:
  def __init__(self):
    self.front = None
    self.rear = None

  def enqueue(self, value):
    node=Node(value)
    if not self.front:
        self.front = node
        self.rear = node
    else:
        self.rear.next = node
        self.rear = self.rear.next

  def dequeue(self):
     if self.front is None:
       raise Exception('its empty')
     dequed=self.front.value
     self.front=self.front.next
     if not self.front:
         self.rear=None
     return dequed

  def is_empty(self):
    return not self.rear

  def peek(self):
      if self.front is None:
        raise Exception("its empty")
      return self.front.value




def breadth_first(tree):
    if tree.root is None:
        return []
    queue=Queue()
    queue.enqueue(tree.root)
    output=[]

    while not queue.is_empty():
        front=queue.dequeue()
        output.append(front.value)
        left=front.left if hasattr(front,'left')else None
        right=front.right if hasattr(front,'right')else None
        if left:
            queue.enqueue(front.left)
        if right:
            queue.enqueue(front.right)
    return output
