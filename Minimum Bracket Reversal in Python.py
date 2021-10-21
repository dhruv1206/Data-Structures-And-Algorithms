'''
🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳
'''
'''
Problem Statement
Given an input string consisting of only { and }, figure out the minimum number of reversals required to make the brackets balanced.

For example:

For input_string = "}}}}, the number of reversals required is 2.
For input_string = "}{}}, the number of reversals required is 1.
If the brackets cannot be balanced, return -1 to indicate that it is not possible to balance them.
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
            temp=self.head
            self.head=self.head.next
        self.num_elements-=1
        return temp.value

    def top(self):
        if self.head is None:
            return None
        return self.head.value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements==0

def minimum_bracket_reversals(my_string):
    extra_moves=0

    if my_string[0]=='}':
        my_string='{'+my_string[1:]
        extra_moves+=1

    if my_string[-1]=="{":
        my_string=my_string[:len(my_string)-1]+"}"
        extra_moves+=1

    prev_char="-"
    if len(my_string)%2!=0:
        return -1

    s=Stack()
    for i in my_string:

        if prev_char+i=="{}":
            _=s.pop()
            prev_char=s.top()

            if s.size()==0:
                prev_char="-"

        else:
            s.push(i)
            prev_char=i

    return int(s.size()/2)+extra_moves

def test_function(test_case):
    input_string = test_case[0]
    expected_output = test_case[1]
    output = minimum_bracket_reversals(input_string)

    if output == expected_output:
        print("Pass")
    else:
        print("Fail")

test_case_1 = ["}}}}", 2]
test_function(test_case_1)

test_case_2 = ["}}{{", 2]
test_function(test_case_2)

test_case_3 = ["{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}", 13]

test_function(test_case_1)


test_case_4= ["}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{", 2]
test_function(test_case_2)

test_case_5 = ["}}{}{}{}{}{}{}{}{}{}{}{}{}{}{}", 1]

test_function(test_case_3)
