# from stack_queue.stack_and_queue import Node,Queue
# # from trees.trees import BinaryTree
# class Node:
#     def __init__(self,value):
#         self.value=value
#         self.children=[]

# def breadth_first(tree):
#     if tree.root is None:
#         return []
#     queue=Queue()
#     queue.enqueue(tree.root)
#     output=[]

#     while not queue.is_empty():
#         front=queue.dequeue()
#         output.append(front.value)
#         for i in range(len(front.children)):
#             queue.enqueue(front.children[i])
#     return output




# class Tree:
#     def __init__(self,root=None):
#         self.root=root

# def fizz_buzz_tree(tree):

#     def traverse(node):
#         if node.children:
#             for i in range(len(node.children)):
#                 traverse(node.children[i])
#                 if node.children[i].value%15==0:
#                         node.children[i].value='fizz buzz'
#                 elif node.children[i].value %3==0:
#                         node.children[i].value="Fizz"
#                 elif node.children[i].value%5==0:
#                         node.children[i].value="Buzz"
#                 else:
#                     node.children[i].value=str(node.children[i].value)
#     traverse(tree.root)
#     if tree.root.value%15==0:
#             tree.root.value='fizz buzz'
#     elif tree.root.value %3==0:
#             tree.root.value="Fizz"
#     elif tree.root.value%5==0:
#             tree.root.value="Buzz"
#     else:
#             tree.root.value=str(tree.root.value)

#     return tree
# def fizz_buzz_tree(tree):
#    root=tree.root
#    fizzlist=[]
#    if root.value is None:
#        return "empty"
#    def traverse(root):
#         if root is None:
#             return
#         if root.value % 15==0:
#                root.value="FizzBuzz"
#         elif root.value %3==0:
#                 root.value="Fizz"
#         elif root.value %5==0:
#                 root.value="Buzz"

#         fizzlist.append(root.value)
#         left=root.left if hasattr(root,'left')else None
#         right=root.right if hasattr(root,'right')else None
#         if left:
#             traverse(root.left)
#         if right:
#             traverse(root.right)
#    traverse(root)
#    return fizzlist


if __name__=="__main__":

    ktree = Node(2)
    ktree.children+= [Node(5)]
    ktree.children+= [Node(5)]
    ktree.children[0].children+= [Node(2)]
    ktree.children[0].children+= [Node(6)]
    ktree.children[0].children[1].children+= [Node(5)]
    ktree.children[0].children[1].children+= [Node(11)]
    ktree.children[1].children+= [Node(9)]
    ktree.children[1].children+= [Node(15)]
    ktree.children[1].children[1].children+= [Node(30)]
    ktree.children[0].children[1].children+= [Node(13)]
    ktree.children[0].children[1].children+= [Node(4)]
    tree1=Tree(ktree)
    after=fizz_buzz_tree(tree1)
    print(breadth_first(after))
    print(ktree.children[1].value)



