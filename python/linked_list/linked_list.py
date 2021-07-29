class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        self.head=None

    def insert(self,value):
        # method body here
        node=Node(value)
        node.next=self.head
        self.head=node

    def includes(self,value):

        current=self.head
        while current:
            if current.value==value:
                return True
            else :
                current=current.next
        return False

    def __str__(self):
        current=self.head
        linkListStr=''
        while True:
            if current!=None:
                linkListStr+="{"+str(current.value)+"}->"
                current=current.next
            elif current==None:
                linkListStr+="Null"
                break
        return linkListStr

   

