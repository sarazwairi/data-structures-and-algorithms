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

  def peek(self):
      if self.top is None:
        raise Exception("its empty")
      return self.top.value


class PseudoQueue:

    def __init__(self):
        self.top = None
        self.main = Stack()
        self.temp = Stack()

    def enqueue(self,value):
        while self.main.top:
            self.temp.push(self.main.top.value)
            self.main.pop()
        self.main.push(value)
        while self.temp.top:
            self.main.push(self.temp.top.value)
            self.temp.pop()
        self.top=self.main.top

    def dequeue(self):
        if self.top:
            output=self.top.value
            self.main.pop()
            self.top=self.main.top
            return output


    