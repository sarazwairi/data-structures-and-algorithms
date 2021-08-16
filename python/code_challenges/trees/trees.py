
class Node:
    def __init__(self,value=None,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

class BinaryTree:

    def __init__(self,root=None):
        self.root=root

    def pre_order(self):
        list=[]
        def preorder(root):
            list.append(root.value)
            if root.left :
                preorder(root.left)

            if root.right :
                preorder(root.right)

        preorder(self.root)
        # print(list)
        return list

    def in_order(self):
        list=[]
        def inorder(root):
            if root.left :
                inorder(root.left)
            list.append(root.value)

            if root.right :
                inorder(root.right)

        inorder(self.root)
        print(list)
        return list


    def post_order(self):
        list=[]
        def postorder(root):
            if root.left :
                postorder(root.left)

            if root.right :
                postorder(root.right)
            list.append(root.value)


        postorder(self.root)
        print(list)
        return list


    def max_value(self):

        if self.root is None:
            return None
        else:
            maxvalue=self.root.value
            def fun(root1,root2,maxvalue):
                if root1:
                  if root1.value >maxvalue:
                       maxvalue=root1.value
                  maxvalue=fun(root1.left,root1.right,maxvalue)
                if root2:
                   if root2.value>maxvalue:
                        maxvalue=root2.value
                   maxvalue=fun(root2.left,root2.right,maxvalue)
                return maxvalue
        maxvalue=fun(self.root.left,self.root.right,maxvalue)
        return maxvalue



class BinarySearchTree(BinaryTree):
    def __init__(self,root=None):
        self.root=root

    def add(self,value):
        new_node=Node(value)
        curr=self.root

        if self.root==None:
            self.root=new_node


        while curr !=None:
            if curr.value>value:
                if curr.left is None:
                    curr.left=new_node
                    return value
                else:
                    curr=curr.left

            else:
                if curr.right is None:
                    curr.right=new_node
                    return value
                else:
                    curr=curr.right

    def contains(self,target):
        if self.root is None:
            return False
        curr =self.root

        while curr:
            if curr.value==target:
                return True
            if target>curr.value:
                curr=curr.right
            else:
                curr=curr.left
        return False








if __name__=="__main__":
    node1=Node(1)
    node1.left=Node(2)
    node1.right=Node(3)
    binary_tree=BinaryTree(node1)
    # binary_tree.pre_order()
    # binary_tree.in_order()
    # binary_tree.post_order()
    # print(binary_tree.max_value())
    # bst=BinarySearchTree()
    # bst.add(1)
    # bst.add(2)
    # bst.add(3)
    # bst.add(6)
    # bst.add(5)
    # bst.add(6)
    # bst.post_order()

