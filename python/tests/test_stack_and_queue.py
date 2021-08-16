import pytest
from code_challenges.stack_queue.stack_and_queue import Stack, Node ,Queue,breadth_first
from code_challenges.trees.trees import BinarySearchTree

@pytest.fixture
def data():
  new_stack = Stack()

  return {'stack':new_stack}



def test_stack_pushing_one_element(data):
  data['stack'].push(1)
  actual = data['stack'].top.value
  expected = 1
  assert actual == expected


@pytest.fixture
def test_stack_pushing_multi_element(new_stack):

  actual = new_stack.top.value
  expected = 2
  assert actual == expected


def test_stack_pop_one_element(data):
    data['stack'].push(1)
    data['stack'].push(2)
    actual = data['stack'].pop()
    expected = 2
    assert expected == actual

def test_stack_is_empty():
  stack = Stack()
  assert stack.is_empty()

def test_stack_is_not_empty():
  stack = Stack()
  stack.top = Node(1)
  assert not stack.is_empty()


def test_peek_empty_stack_raises_exception():
   new_stack=Stack()
   with pytest.raises(Exception):
       new_stack.peek()


@pytest.fixture
def test_peek_the_next_item(new_stack):
    actual = new_stack.peek()
    expected = 2
    assert actual == expected

def test_empty_queue():
    new_queue = Queue()
    assert new_queue.front == None
    assert new_queue.rear == None

def test_enqueue_one_item():
   new_queue = Queue()
   new_queue.enqueue(1)
   assert new_queue.front.value == 1
   assert new_queue.rear.value == 1

@pytest.fixture

def test_enqueue_multi_item(new_queue):
   assert new_queue.front.value == 1
   assert new_queue.next.value == 2
   assert new_queue.rear.value == 3

@pytest.fixture

def test_dequeue(new_queue):
    actual = new_queue.dequeue()
    expected = 1
    assert actual == expected
    assert new_queue.front.value == 2

@pytest.fixture

def test_empty_queue_after_dequeue(new_queue):
    while not new_queue.is_empty():
        new_queue.dequeue()
    assert new_queue.front == None

def test_dequeue_empty_raise_exception():
    new_queue = Queue()
    with pytest.raises(Exception):
        new_queue.dequeue()

def test_peek_empty_raise_exception():
    new_queue = Queue()
    with pytest.raises(Exception):
        new_queue.peek()


def test_breadth_first_tree_empty():
    tree=BinarySearchTree()
    actual=breadth_first(tree)
    assert actual==[]

def test_breadth_first_one_node():
    tree=BinarySearchTree()
    tree.add(5)
    actual=breadth_first(tree)
    assert actual==[5]



def test_breadth_first_correct_order():
    tree=BinarySearchTree()
    input=[10,20,5,4,13,6]
    for item in input:
        tree.add(item)
    actual=breadth_first(tree)
    expected=[10,5,20,4,6,13]
    assert actual==expected
