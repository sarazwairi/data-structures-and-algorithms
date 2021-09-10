from data_structures.hashtable import HashTable
from trees.trees import BinaryTree,Node


def tree_intersection(tree1,tree2):
    # list1=tree1.in_order()
    # list2=tree2.in_order()

    # output=[]

    # for i in list1:
    #     if i in list2:
    #         output.append(i)
    # if output:
    #     return output
    # else:
    #     return None
    ht=HashTable()
    list=[]
    def in_order(node):
        if ht.contains(str(node.value)):
            list=[]

            list+=[node.value]
        else:
            ht.add(str(node.value),True)
        if node.left:
            in_order(node.left)
        if node.right:
            in_order(node.right)
    in_order(tree1.root)
    in_order(tree2.root)
    return list

if __name__=="__main__":
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
    print(tree_intersection(bt,bt1))
