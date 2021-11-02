'''
🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳
'''
class BinaryTreeNode(object):
    def __init__(self , value):
        self.value=value
        self.left=None
        self.right=None

def diameter_of_binary_tree(root):
    if root is None:
        return 0
    else:
        return sum(diameter_of_binary_tree_rec(root))

def diameter_of_binary_tree_rec(root):
    node=root
    left_sum=0
    right_sum=0

    if node is None:
        return 0

    if node.left is not None:
        left_sum=max(diameter_of_binary_tree_rec(node.left))+1
    if node.right is not None:
        right_sum=max(diameter_of_binary_tree_rec(node.right))+1
    return [left_sum , right_sum]

########################TEST CASES#############################
from queue import Queue

def convert_arr_to_binary_tree(arr):
    """
    Takes arr representing level-order traversal of Binary Tree
    """
    index = 0
    length = len(arr)

    if length <= 0 or arr[0] == -1:
        return None

    root = BinaryTreeNode(arr[index])
    index += 1
    queue = Queue()
    queue.put(root)

    while not queue.empty():
        current_node = queue.get()
        left_child = arr[index]
        index += 1

        if left_child is not None:
            left_node = BinaryTreeNode(left_child)
            current_node.left = left_node
            queue.put(left_node)

        right_child = arr[index]
        index += 1

        if right_child is not None:
            right_node = BinaryTreeNode(right_child)
            current_node.right = right_node
            queue.put(right_node)
    return root

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    root = convert_arr_to_binary_tree(arr)
    output = diameter_of_binary_tree(root)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arr = [1, 2, 3, 4, 5, None, None, None, None, None, None]
solution = 3

test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 3, 4, None, 5, None, None, None, None, None]
solution = 4

test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 3, None, None, 4, 5, 6, None, 7, 8, 9, 10, None, None, None, None, None, None, 11, None, None, None]
solution = 6

test_case = [arr, solution]
test_function(test_case)
