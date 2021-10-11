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

class Solution:
    def evalRPN(self, List):
        s=Stack()
        for elements in List:
            if elements in ['+' ,'-' , '*' , '/']:
                element1=s.pop()
                element2=s.pop()
                s.push(str(int(eval(element2+elements+element1))))
            else:
                s.push(elements)
        return s.pop()

        
