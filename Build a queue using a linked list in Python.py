class Node(object):
    def __init__(self , value):
        self.value=value
        self.next=None

class Queue(object):
    def __init__(self):
        self.head=None
        self.num_elements=0

    def enqueue(self , value):
        if self.head is None:
            self.head=Node(value)
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=Node(value)
        self.num_elements+=1

    def dequeue(self):
        if self.head is None:
            return None
        else:
            temp=self.head
            self.head=self.head.next
        self.num_elements-=1
        return temp.value

    def is_empty(self):
        return self.num_elements==0

    def size(self):
        return self.num_elements

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print ("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print ("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail")
