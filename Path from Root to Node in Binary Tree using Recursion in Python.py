'''
🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳
'''
class BinaryTreeNode(object):
    def __init__(self , value):
        self.value=value
        self.left=None
        self.right=None

def path_from_root_to_node(root , value):
    if root.value==value:
        return [value]

    if root.left is None and root.right is None:
        return []
    my_arr_left=[root.value]
    my_arr_right=[root.value]


    if root.left is not None:
        my_arr_left.extend(path_from_root_to_node(root.left , value))
    if root.right is not None:
        my_arr_right.extend(path_from_root_to_node(root.right, value))

    if len(my_arr_right)>len(my_arr_left):
        return my_arr_right
    elif len(my_arr_right)<len(my_arr_left) :
        return my_arr_left
    else:
        return []

####################TESTING####################
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
    data = test_case[1]
    solution = test_case[2]
    root = convert_arr_to_binary_tree(arr)
    output = path_from_root_to_node(root, data)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arr = [1, 2, 3, 4, 5, None, None, None, None, None, None]
data = 5
solution = [1, 2, 5]

test_case = [arr, data, solution]
test_function(test_case)

arr = [1, 2, 3, 4, None, 5, None, None, None, None, None]
data = 5
solution = [1, 3, 5]

test_case = [arr, data, solution]
test_function(test_case)

arr = [1, 2, 3, None, None, 4, 5, 6, None, 7, 8, 9, 10, None, None, None, None, None, None, 11, None, None, None]
data = 11
solution = [1, 3, 4, 6, 10, 11]

test_case = [arr, data, solution]
test_function(test_case)

arr = [1, 2, 3, None, None, 4, 5, 6, None, 7, 8, 9, 10, None, None, None, None, None, None, 11, None, None, None]
data = 8
solution = [1, 3, 5,8]

test_case = [arr, data, solution]
test_function(test_case)
