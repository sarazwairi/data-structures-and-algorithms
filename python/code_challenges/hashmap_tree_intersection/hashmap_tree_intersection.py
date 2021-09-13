from data_structures.hashtable import HashTable
from code_challenges.trees.trees import BinaryTree,Node
from code_challenges.stack_queue.stack_and_queue import Queue

def tree_intersection(tree1, tree2):
    if not tree1.root and not tree2.root:
        return []
    if not tree1.root:
        return []
    if not tree2.root:
        return []
    list = []
    ht = HashTable()
    def in_order(tree, hasht, firsttree=False):
        common = []
        queque = Queue()
        queque.enqueue(tree.root)
        while not queque.is_empty():
            item = queque.dequeue()
            if firsttree:
                hasht.add(item.value, item.value)
            else:
                if hasht.contains(item.value):
                    common += [item.value]
            if item.left if hasattr(item, 'left') else None:
                queque.enqueue(item.left)
            if item.right if hasattr(item, 'right') else None:
                queque.enqueue(item.right)
        return common
    _ = in_order(tree1, ht, True)
    list = in_order(tree2, ht)
    if len(list) > 0:
        return list
    else:
        return []
# def tree_intersection(tree1,tree2):
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
