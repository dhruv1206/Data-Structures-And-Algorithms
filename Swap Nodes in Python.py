'''

🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳

'''
'''
Problem Statement
Given a linked list, swap the two nodes present at position i and j. The positions are based on 0-based indexing.

Example:

linked_list = 3 4 5 2 6 1 9
positions = 3 4
output = 3 4 5 6 2 1 9
Explanation:

The node at position 3 has the value 2
The node at position 4 has the value 6
Swapping these nodes will result in a final order of nodes of 3 4 5 6 2 1 9
'''


class Node(object):
    def __init__(self , value):
        self.value=value
        self.next=None

def swap_nodes(head, left_index, right_index):
    """
    :param: head- head of input linked list
    :param: left_index - indicates position
    :param: right_index - indicates position
    return: head of updated linked list with nodes swapped
    TODO: complete this function and swap nodes present at left_index and right_index
    Do not create a new linked list
    """
    # Values to swap
    node = head
    position = 0
    while position <= right_index:
        if position == left_index:
            left_data = node.value

        if position == right_index:
            right_data = node.value
        position += 1
        node = node.next
    
    # Swapping values
    node = head
    position = 0
    while position <= right_index:
        if position == left_index:
            node.value = right_data

        if position == right_index:
            node.value = left_data
        position += 1
        node = node.next

    return head


def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head):
    while head:
        print(head.value, end=" ")
        head = head.next
    print()

arr = [3, 4, 5, 2, 6, 1, 9]
left_index = 2 
right_index = 4
head = create_linked_list(arr)
print_linked_list(swap_nodes(head,  left_index , right_index))

arr = [3, 4, 5, 2, 6, 1, 9]
left_index = 0
right_index = 1
head = create_linked_list(arr)
print_linked_list(swap_nodes(head,  left_index , right_index))


arr = [3, 4, 5, 2, 6, 1, 9]
head = create_linked_list(arr)
left_index = 3
right_index = 4
print_linked_list(swap_nodes(head,  left_index , right_index))
