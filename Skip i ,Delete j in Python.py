'''

🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳

'''
'''
Problem Statement:
You are given the head of a linked list and two integers, i and j. You have to retain the first i nodes and then delete the next j nodes. Continue doing so until the end of the linked list.

Example:

linked-list = 1 2 3 4 5 6 7 8 9 10 11 12
i = 2
j = 3
Output = 1 2 6 7 11 12
'''
class Node(object):
    def __init__(self , value):
        self.value=value
        self.next=None

def skip_i_delete_j(head , i , j):
    temp=head
    trimmed_linked_list=None
    i_mode=True
    last_node=False
    position_counter=1
    while not last_node:
        if i_mode:
            if trimmed_linked_list is None:
                trimmed_linked_list=Node(temp.value)
            else:
                temp1=trimmed_linked_list
                while temp1.next:
                    temp1=temp1.next
                temp1.next=Node(temp.value)
            if position_counter==i:
                i_mode=False
                position_counter=0
        else:
            if position_counter==j:
                i_mode=True
                position_counter=0
        position_counter+=1
        last_node=temp.next is None
        temp=temp.next

    return trimmed_linked_list

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
        print(head.value, end=' ')
        head = head.next
    print()

def test_function(test_case):
    head = test_case[0]
    i = test_case[1]
    j = test_case[2]
    solution = test_case[3]
        
    temp = skip_i_delete_j(head, i, j)
    index = 0
    try:
        while temp is not None:
            if temp.value != solution[index]:
                print("Fail")
                return
            index += 1
            temp = temp.next
        print("Pass")
    except Exception as e:
        print("Fail")

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i = 2
j = 2
head = create_linked_list(arr)
solution = [1, 2, 5, 6, 9, 10]
test_case = [head, i, j, solution]
test_function(test_case)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i = 2
j = 3
head = create_linked_list(arr)
solution = [1, 2, 6, 7, 11, 12]
test_case = [head, i, j, solution]
test_function(test_case)

arr = [1, 2, 3, 4, 5]
i = 2
j = 4
head = create_linked_list(arr)
solution = [1, 2]
test_case = [head, i, j, solution]
test_function(test_case)


