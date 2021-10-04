'''



🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳



'''
class Node(object):
    
    def __init__(self , value):
        self.value=value
        self.next=None


class LinkedList:
    
    def __init__(self):
        self.head=None

    def prepend(self , value):
        if self.head==None:
            self.head=Node(value)
        else:
            temp=self.head
            self.head=Node(value)
            self.head.next=temp

    def append(self , value):
        temp=self.head
        if temp==None:
            self.head=Node(value)
        else:
            while temp.next!=None:
                temp=temp.next
            temp.next=Node(value)
                
    def search(self , value):
        temp=self.head

        while temp.next!=None:
            if temp.value==value:
                return temp
            temp=temp.next
        return None
    
    def remove(self  , value):
        temp1=self.head
        temp2=None
        while temp1!=None:
            if temp1.value==value:
                if temp2 is None:
                    self.head=temp1.next
                    break
                else:
                    temp2.next=temp1.next
                    break
            temp2=temp1
            temp1=temp1.next

    def pop(self):
        temp=self.head.value
        self.head=self.head.next
        return temp

    def insert(self , value , pos):
        temp1=self.head
        temp2=None
        if pos==0:
            temp2=self.head
            self.head=Node(value)
            self.head.next=temp2
            return
        else:
            for i in range(1 , pos-1):
                if temp1.next is None:
                    temp1.next=Node(value)
                    return
                temp1=temp1.next
            temp2=temp1.next
            temp1.next=Node(value)
            temp1=temp1.next
            temp1.next=temp2
            return

    def size(self):
        len=0 
        temp =self.head
        while temp!=None:
            temp=temp.next
            len+=1 
        return len

    def convert_to_list(self):
        temp=self.head
        my_list=[]
        while temp!=None:
            my_list.append(temp.value)
            temp=temp.next
        return my_list

####################################TESTING########################################


linked_list = LinkedList()
linked_list.prepend(1)
#assert linked_list.convert_to_list() == [1], f"list contents: {linked_list.convert_to_list()}"
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.convert_to_list() == [2, 1, 3], f"list contents: {linked_list.convert_to_list()}"
    
# Test append
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.convert_to_list() == [1], f"list contents: {linked_list.convert_to_list()}"
linked_list.append(3)
assert linked_list.convert_to_list() == [1, 3], f"list contents: {linked_list.convert_to_list()}"

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.convert_to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.convert_to_list()}"

# Test remove
linked_list.remove(1)
assert linked_list.convert_to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.convert_to_list()}"
linked_list.remove(3)
assert linked_list.convert_to_list() == [2, 1, 4, 3], f"list contents: {linked_list.convert_to_list()}"
linked_list.remove(3)
assert linked_list.convert_to_list() == [2, 1, 4], f"list contents: {linked_list.convert_to_list()}"

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.convert_to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.convert_to_list()}"

# Test insert 
linked_list.insert(5, 0)
assert linked_list.convert_to_list() == [5, 1, 4], f"list contents: {linked_list.convert_to_list()}"
linked_list.insert(2, 1)
assert linked_list.convert_to_list() == [5, 2, 1, 4], f"list contents: {linked_list.convert_to_list()}"
linked_list.insert(3, 6)
assert linked_list.convert_to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.convert_to_list()}"

# Test size
assert linked_list.size() == 5, f"list contents: {linked_list.convert_to_list()}"
