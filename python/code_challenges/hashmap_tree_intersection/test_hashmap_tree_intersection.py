from code_challenges.trees.trees import BinaryTree,Node
from code_challenges.hashmap_tree_intersection.hashmap_tree_intersection import tree_intersection

def test_empty_tree():
    tree1=BinaryTree()
    tree2=BinaryTree()
    actual=tree_intersection(tree1,tree2)
    expect=[]
    assert actual== expect



def test_one_tree():
    bt = BinaryTree()
    bt1 = BinaryTree()
    bt1.root = Node("12")
    bt1.root.right = Node("100")
    bt1.root.left = Node("200")
    bt1.root.left.left = Node("100")
    bt1.root.left.right = Node("50")
    bt1.root.right.left = Node("60")
    assert [] == tree_intersection(bt, bt1)


def test_common_values():
    bt = BinaryTree()
    bt1 = BinaryTree()
    bt.root = Node("100")
    bt.root.right = Node("20")
    bt.root.left = Node("50")
    bt.root.left.left = Node("5")
    bt.root.left.right = Node("15")
    bt1.root = Node("20")
    bt1.root.right = Node("150")
    bt1.root.left = Node("100")
    bt1.root.left.left = Node("5")
    bt1.root.left.right = Node("6")
    bt1.root.right.left = Node("7")
    assert ['20','100','5'] == tree_intersection(bt, bt1)
