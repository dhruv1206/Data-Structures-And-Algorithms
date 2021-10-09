'''

🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳

'''
'''
Problem Statement:
Given a linked list, swap the two nodes present at position i and j. The positions are based on 0-based indexing.

Note: You have to swap the nodes and not just the values.

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
    if left_index==right_index:
        return

    prevX=None
    currX=head
    position_counter=0
    while currX is not None and position_counter!=left_index:
        prevX=currX
        currX=currX.next
        position_counter+=1 

    prevY=None
    currY=head
    position_counter=0
    while currY is not None and position_counter!=right_index:
        prevY=currY
        currY=currY.next
        position_counter+=1 

    if currY is None or currX is None:
        return

    if prevX is not None:
        prevX.next=currY
    else:
        head=currY

    if prevY is not None:
        prevY.next=currX
    else:
        head=currX

    temp=currX.next
    currX.next=currY.next
    currY.next=temp
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

################TESTING################
def test_function(test_case):
    head = test_case[0]
    left_index = test_case[1]
    right_index = test_case[2]
    
    left_node = None
    right_node = None
    
    temp = head
    index = 0
    try:
        while temp is not None:
            if index == left_index:
                left_node = temp
            if index == right_index:
                right_node = temp
                break
            index += 1
            temp = temp.next

        updated_head = swap_nodes(head, left_index, right_index)

        temp = updated_head
        index = 0
        pass_status = [False, False]

        while temp is not None:
            if index == left_index:
                pass_status[0] = temp is right_node
            if index == right_index:
                pass_status[1] = temp is left_node

            index += 1
            temp = temp.next

        if pass_status[0] and pass_status[1]:
            print("Pass")
        else:
            print("Fail")
        return updated_head
    except Exception as e:
        print("Fail")

arr = [3, 4, 5, 2, 6, 1, 9]
head = create_linked_list(arr)
left_index = 3
right_index = 4

test_case = [head, left_index, right_index]
updated_head = test_function(test_case)

arr = [3, 4, 5, 2, 6, 1, 9]
left_index = 2 
right_index = 4
head = create_linked_list(arr)
test_case = [head, left_index, right_index]
updated_head = test_function(test_case)

arr = [3, 4, 5, 2, 6, 1, 9]
left_index = 0
right_index = 1
head = create_linked_list(arr)
test_case = [head, left_index, right_index]
updated_head = test_function(test_case)

