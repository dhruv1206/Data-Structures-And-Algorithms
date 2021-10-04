'''
🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳
'''
class Node(object):
    
    def __init__(self , value):
        self.value=value
        self.next=None
def print_list(head):
    temp=head
    while temp!=None:
        print(temp.value , end=" ")
        temp=temp.next

class LinkedList:
    
    def __init__(self):
        self.head=None

    def append(self , value):
        if self.head is None:
            self.head=Node(value)
            return
        
        temp=self.head
    
        while temp.next:
            temp=temp.next
        temp.next=Node(value)
            
    
def insert_at_head(linked_list , value):
    temp=linked_list.head
    linked_list.head=Node(value)
    linked_list.head.next=temp
    return linked_list

def reverse(linked_list):
    temp=linked_list.head
    reversed_linked_list=LinkedList()
    while temp is not None:
        value=temp.value
        reversed_linked_list= insert_at_head(reversed_linked_list , value)
        temp=temp.next
    return reversed_linked_list


llist = LinkedList()
for value in [4,2,5,1,-3,0]:
    llist.append(value)
flipped = reverse(llist)
print_list(llist.head)
print()
print_list(flipped.head)
