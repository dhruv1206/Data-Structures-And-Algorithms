class Node(object):
    def __init__(self , value):
        self.value=value
        self.next=None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self ,head ):
        self.head=head

    def append(self , value):
        if self.head is None:
            self.head=Node(value)
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=Node(value)
        return

    def flatten_deep(self):
        value_list=[]
        temp=self.head
        while temp:
            value_list.append(temp.value)
            temp=temp.next
        return value_list

    def __iter__(self):
        temp=self.head
        while temp:
            yield temp.value
            temp=temp.next

# def merge(list1, list2):
#     merged=LinkedList(None)

#     if list1 is None:
#         return list2
#     if list2 is None:
#         return list1

#     temp1=list1.head
#     temp2=list2.head

#     while temp1 is not None or temp2 is not None:
#         if temp1 is None:
#             merged.append(temp2)
#             temp2=temp2.next
#         elif temp2 is None:
#             merged.append(temp1)
#             temp1=temp1.next
#         elif temp1.value<=temp2.value:
#             merged.append(temp1)
#             temp1=temp1.next
#         elif temp2.value<=temp1.value:
#             merged.append(temp2)
#             temp2=temp2.next
#     return merged


class NestedLinkedList(LinkedList):
    def flatten(self):
        values=[]
        for elements in self.flatten_deep():
            values.append(elements)
        values=[item for sublist in values for item in sublist]
        values.sort()
        return values
#%% First Challenge - Definition
linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

nested_linked_list = NestedLinkedList(Node(linked_list))
nested_linked_list.append(second_linked_list)

#%% First Challenge - Solution
solution = nested_linked_list.flatten()
print(solution)

