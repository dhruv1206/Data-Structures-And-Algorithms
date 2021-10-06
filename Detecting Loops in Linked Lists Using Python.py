'''

🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳

'''

'''
---------------APPROACH TO THE PROBLEM---------------

If a loop exists in the list, the fast runner will eventually 
move behind the slow runner as it moves to the beginning of the loop.
Eventually it will catch up to the slow runner and both runners will 
be pointing to the same node at the same time. If this happens then you
know there is a loop in the linked list.


'''

class Node(object):
    def __init__(self ,value):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self , my_list=None):
        self.head=None
        if my_list:
            for i in my_list:
                self.append(i)
    def append(self , value):
        if self.head is None:
            self.head=Node(value)
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=Node(value)
        return



def iscircular(linked_list):
    if linked_list.head is None:
        return False
    slow=linked_list.head
    fast=linked_list.head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next. next

        if slow==fast:
            return True

'''
---------------TESTING---------------

'''

list_with_loop=LinkedList([2,-1,3,0,5])
loop_start=list_with_loop.head.next     #Creating a loop where the last node points back to the second node
node=list_with_loop.head
while node.next:
    node=node.next
node.next=loop_start

small_loop = LinkedList([0])
small_loop.head.next = small_loop.head

#SOME TEST CASES
print ("Pass" if iscircular(list_with_loop) else "Fail")
print ("Pass" if not iscircular(LinkedList([-4, 7, 2, 5, -1])) else "Fail")
print ("Pass" if not iscircular(LinkedList([1])) else "Fail")
print ("Pass" if iscircular(small_loop) else "Fail")
print ("Pass" if not iscircular(LinkedList([])) else "Fail")
