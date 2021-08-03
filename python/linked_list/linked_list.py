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

# code challenge 7:

    def append(self,value):
        node1=Node(value)
        if not self.head:
            self.head=node1
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=node1


    def insert_Before(self,targeted_node,value):
        new_node=Node(value)
        node1=self.head
        if node1==None:
           print('no nodes')
        else:
            found=False
            while node1:
                if node1.next==None:
                  break
                if node1.next.value==targeted_node:
                   found=True
                   new_node.next=node1.next
                   node1.next=new_node
                   break
                else:
                  node1=node1.next
            if found !=True:
               print('targeted node not found')

    def insert_After(self,targeted_node,value):
        new_node=Node(value)
        node1=self.head
        while(node1):
            if node1.value==targeted_node:
                new_node.next=node1.next
                node1.next=new_node
                break


# code challenge 7:

    def kthFromEnd(self,k):
        try:
            if k<0 :
                    return 'negative'
            current=self.head
            values=[]
            while(current.next!=None):
                    values.append(current.value)
                    current=current.next
            else:
                values.append(current.value)
                    # values.reverse()
                return values[::-1][k]
        except:
                return ('short link_list')






l1=LinkedList()
l1.append(2)
l1.append(5)
l1.append(20)
# print(l1.kthFromEnd(1))
