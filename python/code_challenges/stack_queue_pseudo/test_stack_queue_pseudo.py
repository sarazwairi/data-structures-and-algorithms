import pytest
from stack_queue_pseudo import Stack, Node ,PseudoQueue


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


def test_peek_empty_stack_raises_exception():
   new_stack=Stack()
   with pytest.raises(Exception):
       new_stack.peek()


@pytest.fixture
def test_peek_the_next_item(new_stack):
    actual = new_stack.peek()
    expected = 2
    assert actual == expected


#PseudoQueue

def test_enqueue_empty_PseudoQueue():
    queue = PseudoQueue()
    queue.enqueue(1)
    actual=queue.top.value
    expected=1
    assert actual==expected


def test_multi_enqueue_PseudoQueue():
    queue = PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    actual=queue.top.value
    expected=1
    assert actual==expected

def test_dequeue_PseudoQueue():
    queue = PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    actual=queue.dequeue()
    expected=1
    assert actual==expected

def test_multi_dequeue_PseudoQueue():
    queue = PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    queue.dequeue()

    actual=queue.dequeue()
    expected=3
    assert actual==expected


def test_dequeue_from_empty_PseudoQueue():
    queue = PseudoQueue()
    actual=queue.dequeue()
    expected=None
    assert actual==expected
