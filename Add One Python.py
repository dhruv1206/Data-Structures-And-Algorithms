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
