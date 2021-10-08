'''
🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳

'''
'''
Problem Statement:
You are given a non-negative number in the form of list elements. For example, the number 123 would be provided as arr = [1, 2, 3]. Add one to the number and return the output in the form of a new list.

Example 1:

input = [1, 2, 3]
output = [1, 2, 4]
Example 2:

input = [9, 9, 9]
output = [1, 0, 0, 0]
Challenge:

One way to solve this problem is to convert the input array into a number and then add one to it. For example, if we have input = [1, 2, 3], you could solve this problem by creating the number 123 and then separating the digits of the output number 124.


'''

def list_to_string(my_list):
    string=str()
    for i in my_list:
        string+=str(i)
    return string

def string_to_num(string):
    number=int(string)
    number+=1
    return str(number)

def string_to_list(string):
    my_list=[]
    for i in string:
        my_list.append(i)
    return my_list

def add_one(my_list):
    return string_to_list(string_to_num(list_to_string(my_list)))

print(add_one([9,9,9]))
