# from stack_queue.stack_and_queue import Node
# from trees.trees import BinaryTree


class Node:
    def __init__(self,value):
        self.value=value
        self.children=[]

class tree:
    def __init__(self):
        self.root=None


def fizz_buzz_tree(tree):

    def traverse(node):
        if node.children:
            for i in range(len(node.children)):
                traverse(node.children[i])
                if node.children[i].value%15==0:
                        node.children[i].value='fizz buzz'
                elif node.children[i].value %3==0:
                        node.children[i].value="Fizz"
                elif node.children[i].value%5==0:
                        node.children[i].valu="Buzz"
                else:
                    node.children[i].value=str(node.children[i].value)
    traverse(tree.root)
    if tree.root.value%15==0:
            tree.root.value='fizz buzz'
    elif tree.root.value %3==0:
            tree.root.value="Fizz"
    elif tree.root.value%5==0:
            tree.root.valu="Buzz"
    else:
            tree.root.value=str(tree.root.value)

    return tree
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
    ktree =tree()
    ktree.root = Node(2)
    ktree.root.children+= [Node(5)]
    ktree.root.children+= [Node(5)]
    ktree.root.children[0].children+= [Node(2)]
    ktree.root.children[0].children+= [Node(6)]
    ktree.root.children[0].children[1].children+= [Node(5)]
    ktree.root.children[0].children[1].children+= [Node(11)]
    ktree.root.children[1].children+= [Node(9)]
    ktree.root.children[1].children+= [Node(15)]
    ktree.root.children[1].children[1].children+= [Node(30)]
    ktree.root.children[0].children[1].children+= [Node(13)]
    ktree.root.children[0].children[1].children+= [Node(4)]

    after=fizz_buzz_tree(ktree)
    print(after)
    print(ktree.root.children[1].value)
