'''
🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳
'''

class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()


def equation_checker(string):
    s=Stack()
    counter=0
    for i in string:
        if i == '[' or i == '{' or i == '(':
            s.push(i)
            counter+=1
        elif i == ']':
            if s.pop()=='[':
                counter-=1
            else:
                return False
        elif i == '}':
            if s.pop()=='{':
                counter-=1
            else:
                return False
        elif i == ')':
            if s.pop()=='(':
                counter-=1
            else:
                return False
    if counter==0:
        return True
    else:
        return False

print(equation_checker("{ { } [ ] [ [ [ ] ] ] }"))
