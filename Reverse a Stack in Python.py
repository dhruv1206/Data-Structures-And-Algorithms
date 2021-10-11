'''
🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳
'''
'''
Problem Statement
Reverse a stack. If your stack initially has 1, 2, 3, 4 (4 at the top and 1 at the bottom), after reversing the order must be 4, 3, 2, 1 (4 at the bottom and 1 at the top).
'''

class Node(object):
    def __init__(self , value):
        self.value=value
        self.next=None

class Stack(object):
    def __init__(self):
        self.head=None
        self.num_elements=0

    def push(self , value):
        if self.head is None:
            self.head=Node(value)
        else:
            temp=self.head
            self.head=Node(value)
            self.head.next=temp
        self.num_elements+=1

    def pop(self):
        if self.head is None:
            return None
        else:
            temp=self.head.value
            self.head=self.head.next
        self.num_elements-=1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements==0

def reverse_stack(stack):
    inverse_stack=Stack()

    while not stack.is_empty():
        inverse_stack.push(stack.pop())

    return inverse_stack

def test_function(test_case):
    stack = Stack()
    for num in test_case:
        stack.push(num)

    reverse_stack(stack)
    index = 0
    while not stack.is_empty():
        popped = stack.pop()
        if popped != test_case[index]:
            print("Fail")
            return
        else:
            index += 1
    print("Pass")

test_case_1 = [1, 2, 3, 4]
test_function(test_case_1)

test_case_2 = [1]
test_function(test_case_2)
