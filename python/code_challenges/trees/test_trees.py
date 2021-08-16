import pytest
from trees import Node,BinaryTree,BinarySearchTree



# Can successfully instantiate an empty tree

def test_instantiate_an_empty_tree():
    tree=BinaryTree(Node())
    actual=tree.root.value
    expected=None
    assert actual== expected

# Can successfully instantiate a tree with a single root node

def test_instantiate_a_tree_with_a_single_root_node():
    tree=BinaryTree(Node(10))
    actual=tree.root.value
    expected=10
    assert actual== expected

# Can successfully add a left child and right child to a single root node

def test_add_left_right():
    tree=BinarySearchTree()
    tree.add(5)
    actual=tree.root.value
    expected=5
    assert actual== expected

# Can successfully return a collection from a preorder traversal

def test_pre_order():
    tree=BinaryTree()
    tree.root=Node(1)
    tree.root.left=Node(5)
    tree.root.right=Node(4)
    tree.root.left.left=Node(3)
    tree.root.right.right=Node(2)
    actual=tree.pre_order()
    expected=[1,5,3,4,2]
    assert actual==expected


# Can successfully return a collection from an inorder traversal

def test_in_order():
    tree=BinaryTree()
    tree.root=Node(1)
    tree.root.left=Node(5)
    tree.root.right=Node(4)
    tree.root.left.left=Node(3)
    tree.root.right.right=Node(2)
    actual=tree.in_order()
    expected=[3,5,1,4,2]
    assert actual==expected


# Can successfully return a collection from a postorder traversal

def test_post_order():
    tree=BinaryTree()
    tree.root=Node(1)
    tree.root.left=Node(5)
    tree.root.right=Node(4)
    tree.root.left.left=Node(3)
    tree.root.right.right=Node(2)
    actual=tree.post_order()
    expected=[3,5,2,4,1]
    assert actual==expected


def test_max_value():
    tree=BinaryTree(Node())
    tree.root=Node(1)
    tree.root.left=Node(5)
    tree.root.right=Node(4)
    tree.root.left.left=Node(3)
    tree.root.right.right=Node(2)
    actual=tree.max_value()
    expected=5
    assert actual== expected

def test_max_none():
    empty=BinaryTree()
    actual=empty.max_value()
    expected=None
    assert actual==expected


def test_max_value_false():
    tree=BinaryTree(Node())
    tree.root=Node(1)
    tree.root.left=Node(5)
    tree.root.right=Node(4)
    tree.root.left.left=Node(3)
    tree.root.right.right=Node(2)
    assert tree.max_value()!= 4

