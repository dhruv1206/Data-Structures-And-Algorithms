'''

🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳

'''

class Node(object):
    def __init__(self , value):
        self.value=value
        self.next=None

def create_linked_list(arr):
    if len(arr)==0:
        return None
    head=Node(arr[0])
    temp=head
    for data in arr[1:]:
        temp.next=Node(data)
        temp=temp.next
    return head

def even_after_odd(head):
    temp=head
    even_linked_list=None
    odd_linked_list=None
    while temp:
        if temp.value%2==0:
            if even_linked_list is None:
                even_linked_list=Node(temp.value)
            else:
                temp1=even_linked_list
                while temp1.next:
                    temp1=temp1.next
                temp1.next=Node(temp.value)
        else:
            if odd_linked_list is None:
                odd_linked_list=Node(temp.value)
            else:
                temp1=odd_linked_list
                while temp1.next:
                    temp1=temp1.next
                temp1.next=Node(temp.value)

        temp=temp.next
    if odd_linked_list is None:
        return even_linked_list
    else:    
        temp1=odd_linked_list
        while temp1.next:
            temp1=temp1.next
        temp1.next=even_linked_list
        return odd_linked_list

def print_linked_list(head):
    temp=head
    my_list=[]
    while temp:
        my_list.append(temp.value)
        temp=temp.next
    return my_list

arr1 = [1, 2, 3, 4, 5, 6]
print(print_linked_list(even_after_odd(create_linked_list(arr1))))
arr2 = [1, 3, 5, 7]
print(print_linked_list(even_after_odd(create_linked_list(arr2))))
arr3 = [2, 4, 6, 8]
print(print_linked_list(even_after_odd(create_linked_list(arr3))))
