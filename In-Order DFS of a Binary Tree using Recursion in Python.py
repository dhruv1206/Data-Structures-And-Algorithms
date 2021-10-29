'''
🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳
'''

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

def in_order(tree):
    root=tree.get_root()

    def traverse(node):
        if (not node.has_left_child()) and  (not node.has_right_child()):
            return [node.get_value()]
        visit_order=[]
        if node.has_left_child():
            visit_order.extend(traverse(node.get_left_child()))
        visit_order.extend([node.get_value()])
        if node.has_right_child():
            visit_order.extend(traverse(node.get_right_child()))
        return visit_order

    return traverse(root)




tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

print(in_order(tree))
