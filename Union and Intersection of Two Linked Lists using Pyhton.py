'''
🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳
'''


class Node:
    def __init__(self ,value):
        self.value=value
        self.next=None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head=None

    def __str__(self):
        temp=self.head
        my_list=''
        while temp:
            my_list+=str(temp.value)+'->'
            temp=temp.next
        return my_list

    def append(self , value):
        if self.head is None:
            self.head=Node(value)
            return
        temp=self.head
        while temp.next:
            temp=temp.next

        temp.next=Node(value)

    def size(self):
        size=0
        temp=self.head
        while temp:
            size+=1
            temp=temp.next
        return size

    def to_list(self):
        my_arr=[]
        temp=self.head
        while temp:
             my_arr.append(temp.value)
             temp=temp.next
        return my_arr

    # def __repr__(self):
    #     temp=self.head
    #     my_list=[]
    #     while temp:
    #         my_list.append(temp.value)
    #         temp=temp.next
    #     return my_list

def union(linkedlist1:LinkedList , linkedlist2:LinkedList):
    my_list=list(set(linkedlist1.to_list()+linkedlist2.to_list()))
    my_linked_list=LinkedList()
    for i in my_list:
        my_linked_list.append(i)
    return my_linked_list

def intersection(linkedlist1:LinkedList , linkedlist2:LinkedList):
    my_list1=linkedlist1.to_list()
    my_list2=linkedlist2.to_list()
    my_linked_list=LinkedList()
    for i in my_list1:
        if i in my_list2:
            my_linked_list.append(i)

    return my_linked_list


#%% Test Official
# Normal Cases:
# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
# 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 ->
print(intersection(linked_list_1, linked_list_2))
# 4 -> 6 -> 21 ->

# Test case 2
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
# 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 ->
print(intersection(linked_list_3, linked_list_4))
#

# Test case 3
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [22, 7, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 65, 11, 21, 1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))
# 65 -> 1 -> 35 -> 4 -> 3 -> 6 -> 7 -> 8 -> 11 -> 21 -> 22 -> 23 ->
print(intersection(linked_list_5, linked_list_6))
# 65 -> 7 ->


# Edge Cases:
# Test case 4
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = [1, 7, 8]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print(union(linked_list_7, linked_list_8))
# 8 -> 1 -> 7 ->
print(intersection(linked_list_7, linked_list_8))
#

# Test case 5
linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_9.append(i)

for i in element_2:
    linked_list_10.append(i)

print(union(linked_list_9, linked_list_10))
#
print(intersection(linked_list_9, linked_list_10))
#
