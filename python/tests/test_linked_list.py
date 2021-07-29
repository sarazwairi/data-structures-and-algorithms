from linked_list.linked_list import LinkedList


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






