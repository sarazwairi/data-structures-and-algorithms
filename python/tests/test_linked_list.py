from linked_list.linked_list import LinkedList
from code_challenges.linked_list_zip import zipLists



def test_import():
    assert LinkedList

# Can properly return a collection of all the values that exist in the linked list

# Can successfully instantiate an empty linked list
def test_instantiate_an_empty_linked_list():
    actual=LinkedList().head
    excepted=None
    assert actual==excepted

# Can properly insert into the linked list
def test_insert_into_the_linked_list():
    l1=LinkedList()
    value=100
    l1.insert(value)
    actual1=l1.head.value
    actual2=l1.head.next
    excepted1=100
    excepted2=None
    assert actual1==excepted1
    assert actual2==excepted2

# The head property will properly point to the first node in the linked list
# Can properly insert multiple nodes into the linked list

def test_head():
    l1=LinkedList()
    node1=l1.insert('200')
    assert l1.head.value=='200'


# Will return true when finding a value within the linked list that exists

def test_insert_multiple():
    l1=LinkedList()
    l1.insert('27')
    l1.insert('4')
    l1.insert('1988')
    include1=l1.includes('1988')
    include2=l1.includes('4')
    include3=l1.includes('27')
    assert include1==True
    assert include2==True
    assert include3==True

# Will return false when searching for a value in the linked list that does not exist

def test_false():
    l1=LinkedList()
    l1.insert('1988')
    l1.insert('4')
    include1=l1.includes('1955')
    assert include1==False

# Can properly return a collection of all the values that exist in the linked list

def test_all_values():
    l1=LinkedList()
    l1.insert('10')
    l1.insert('20')
    l1.insert('30')
    assert str(l1)=="{30}->{20}->{10}->Null"





# code challenge 7:

# Can successfully add a node to the end of the linked list

def test_append():
    l1=LinkedList()
    l1.append(10)
    assert l1.head.value is 10
    l1.append(20)
    assert l1.head.next.value is 20
    assert l1.head.next.next is None

def test_insert_Before():
    l1=LinkedList()
    l1.append(1)
    l1.append(2)
    l1.append(3)
    l1.insert_Before(2,40)
    assert l1.head.next.value==40
    l1.insert_Before(40,60)
    assert l1.head.next.value==60

def test_insert_After():
    l1=LinkedList()
    l1.append(1)
    l1.append(2)
    l1.append(3)
    l1.insert_Before(2,40)
    assert l1.head.next.value==40

def test_kthFromEnd():
    l1=LinkedList()
    l1.append(2)
    l1.append(3)
    l1.append(20)
    assert l1.kthFromEnd(1)==3
    assert l1.kthFromEnd(3)=='short link_list'
    assert l1.kthFromEnd(-1)=='negative'


def test_zipLists_first_longer():
    l2=LinkedList()
    l2.append(5)
    l2.append(9)
    l1=LinkedList()

    l1.append(1)
    l1.append(3)
    l1.append(2)

    actual=zipLists(l1,l2)
    expected="{1}->{5}->{3}->{9}->{2}->Null"
    assert actual==expected


def test_zipLists_second_longer():
    l2=LinkedList()
    l2.append(5)
    l2.append(9)
    l2.append(10)
    l2.append(4)
    l1=LinkedList()
    l1.append(1)
    l1.append(3)
    actual=zipLists(l1,l2)
    expected="{1}->{5}->{3}->{10}->{4}->Null"
    assert actual==expected



def test_zipLists_equal():
    l2=LinkedList()
    l2.append(5)
    l2.append(9)
    l2.append(4)
    l1=LinkedList()
    l1.append(1)
    l1.append(3)
    l1.append(2)
    actual=zipLists(l1,l2)
    expected="{1}->{5}->{3}->{9}->{2}->{4}->Null"
    assert actual==expected
