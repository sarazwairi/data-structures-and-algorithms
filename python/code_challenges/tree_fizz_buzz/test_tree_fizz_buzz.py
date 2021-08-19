from tree_fizz_buzz.tree_fizz_buzz import fizz_buzz_tree,Tree,Node


def test_tree_empty():
    tree=Tree(Node())
    actual=fizz_buzz_tree(tree)
    expected="empty"
    assert actual==expected

