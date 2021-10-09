'''

🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳

'''


class Stack(object):
    def __init__(self , size=10):
        self.arr=[0 for i in range(size)]
        self.next_index=0
        self.num_elements=0

    def push(self , element):
        if self.next_index==len(self.arr):
            self._handle_stack_capacity_full()
        self.arr[self.next_index]=element
        self.next_index+=1
        self.num_elements+=1

    def _handle_stack_capacity_full(self):
        old_arr=self.arr

        self.arr=[0 for i in range(2*(len(old_arr)))]
        for index , value in enumerate(old_arr):
            self.arr[index]=value
    def pop(self):
        if self.is_empty():
            return None
        temp=self.arr[self.next_index-1]
        del(self.arr[self.next_index])
        self.num_elements-=1
        self.next_index-=1
        return  temp

    
    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements==0

