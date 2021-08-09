from typing import Counter


class Node:
    def __init__(self,value,next=None):
        self.value=value
        self.next=next

class AnimalShelter :
   def __init__(self):
        self.front=None

   def enqueue(self,value=None):
       node=Node(value)
       if not self.front:
           self.front=node
       else:
           curr=self.front
           while curr.next:
               curr=curr.next
           curr.next=node

   def dequeue(self,pref=None):
       curr=self.front
       if not curr:
           return "no animals"
       if not pref:
           new=self.front
           self.front=curr.next
           return new.value
       if pref != "cat" and pref !="dog":
           return "none"
       while curr.value != pref:
           if curr.next:
               prev=curr
               curr=curr.next
               next_node=curr.next
           else:
               return "none"
       prev.next=next_node
       return curr.value

