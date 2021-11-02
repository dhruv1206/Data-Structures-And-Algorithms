'''
🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳
'''
from collections import deque

class Node(object):
    def __init__(self , value=None):
        self.value=value
        self.left=None
        self.right=None

    def get_value(self):
        return self.value

    def set_value(self ,value):
        self.value=value

    def set_left_child(self , node):
        self.left=node

    def set_right_child(self , node):
        self.right=node

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left!=None

    def has_right_child(self):
        return self.right!=None



# class Tree(object):
#     def __init__(self , value=None):
#         self.root=Node(value)

#     def get_root(self):
#         return self.root

class BST(object):
    def __init__(self):
        self.root=None

    def set_root(self , value):
        self.root=Node(value)

    def get_root(self):
        return self.root

    def compare(self , node , new_node):
        if node.get_value()==new_node.get_value():
            return 1

        elif node.get_value()>new_node.get_value():
            return -1

        else:
            return 0

    def insert_with_loop(self , value):
        new_node=Node(value)
        node=self.get_root()
        if node == None:
            self.set_root(value)
            return
        while True:
            if self.compare(node,new_node)==-1:
                if node.get_left_child() is None:
                    node.set_left_child(new_node)
                    break
                else:
                    node=node.get_left_child()
            elif self.compare(node,new_node)==1:
                break

            else:
                if node.get_right_child() is None:
                    node.set_right_child(new_node)
                    break
                else:
                    node=node.get_right_child()

    def insert_with_recursion(self , value):
        node=self.get_root()

        if node is None:
            self.set_root(value)
        else:
            self.insert_with_recursion_rec(node , value)

    def insert_with_recursion_rec(self , node , value):
        new_node=Node(value)
        if node is None:
            self.root=new_node
            return
        if self.compare(node , new_node)==-1:
            if node.get_left_child():
                self.insert_with_recursion_rec(node.get_left_child() , value)
            else:
                node.set_left_child(new_node)
        elif self.compare(node , new_node)==0:
            if node.get_right_child():
                self.insert_with_recursion_rec(node.get_right_child() , value)
            else:
                node.set_right_child(new_node)
        else:
            return

    def search(self , value):
        node=self.get_root()
        new_node=Node(value)
        if node is None:
            print("Tree is empty!")
            return False
        else:
            return self.search_rec(node ,new_node)


    def search_rec(self ,node , new_node):
        comparison=self.compare(node,new_node)
        if comparison==-1:
            if node.get_left_child() is None:
                print("Number not found!")
                return False
            elif node.get_left_child().get_value()==new_node.get_value():
                print("Number Found!")
                return True
            else:
                self.search_rec(node.get_left_child() , new_node)
        elif comparison==0:
            if node.get_right_child() is None:
                print("Number not found!")
                return False
            elif node.get_right_child().get_value()==new_node.get_value():
                print("Number Found!")
                return True
            else:
                self.search_rec(node.get_right_child() , new_node)
        else:
            print("Number Found!")
            return True

    def minValueNode(self , node):
        while node.get_left_child():
            node=node.get_left_child()
        return node

    def delete(self , value):
        node=self.get_root()
        return self.delete_rec(node , value)
    def delete_rec(self, root,key):
        if root is None:
            return root

        if key<root.get_value():
            root.set_left_child(self.delete_rec(root.get_left_child() , key))

        elif key>root.get_value():
            root.set_right_child(self.delete_rec(root.get_right_child() , key))

        else:
            if root.get_left_child() is None:
                temp=root.get_right_child()
                root=None
                return temp
            elif root.get_right_child() is None:
                temp=root.get_left_child()
                root=None
                return temp

            temp=minValueNode(root.get_right_child())
            root.set_value(temp.get_value())
            root.set_right_child(delete_rec(root.get_right_child() , temp.get_value()))
        return root


def bfs(tree):
    visit_order=[]
    q=Queue()
    q.enq(tree.get_root())
    while len(q)!=0:
        node=q.deq()
        visit_order.append(node.get_value())
        if node.has_left_child():
            q.enq(node.get_left_child())
        if node.has_right_child():
            q.enq(node.get_right_child())

    return visit_order
#DFS function can be found over here :
'''
    In-Order-> https://github.com/dhruv1206/Data-Structures-And-Algorithms-using-Python/blob/main/In-Order%20DFS%20of%20a%20Binary%20Tree%20using%20Recursion%20in%20Python.py
    Post-Order->https://github.com/dhruv1206/Data-Structures-And-Algorithms-using-Python/blob/main/Post-Order%20DFS%20of%20a%20Binary%20Tree%20using%20Recursion%20in%20Python.py
    Pre-Order->https://github.com/dhruv1206/Data-Structures-And-Algorithms-using-Python/blob/main/Pre-Order%20DFS%20of%20a%20Tree%20using%20Recursion%20in%20Python.py
'''

class Queue():
    def __init__(self):
        self.q = deque()

    def enq(self,value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)


bst1 = BST()
bst1.insert_with_loop(5)
bst1.insert_with_loop(6)
bst1.insert_with_loop(4)
bst1.insert_with_loop(2)
bst1.insert_with_loop(5) # insert duplicate
print(bfs(bst1),end=" ")
print("->BST USING LOOP!")
bst = BST()
bst.insert_with_recursion(5)
bst.insert_with_recursion(6)
bst.insert_with_recursion(4)
bst.insert_with_recursion(2)
bst.insert_with_recursion(5) # insert duplicate
print(bfs(bst) , end=" ")
print("->BST USING RECURSION!")
(bst.search(10))
bst.search(2)
(bst.delete(2))
(bst.search(2))
