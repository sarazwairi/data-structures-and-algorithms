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



open_bracket=("[","{","(")
close_bracket=("]","}",")")

def  validate_brackets(str):
    stack=Stack()

    for i in str:
        if i in open_bracket:
            stack.push(i)
        elif i in close_bracket:
            y=close_bracket.index(i)
            if (Stack.top.value==open_bracket(y)):
                stack.pop()
            else:
                return False
        if not stack.top:
            return True
        else:
            return False

