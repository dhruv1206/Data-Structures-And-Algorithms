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



class Tree(object):
    def __init__(self , value=None):
        self.root=Node(value)

    def get_root(self):
        return self.root

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


tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

print(bfs(tree))
