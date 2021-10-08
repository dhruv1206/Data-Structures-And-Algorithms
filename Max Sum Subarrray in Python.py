'''

🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳

'''



def sum_list(my_list):
    result=0
    for i in my_list:
        result+=i
    return result

def sublist_generator(my_list):
    length=len(my_list)+1
    list_of_lists=[]

    for i in range(length):
        for j in range(i+1,length):
            list_of_lists.append(my_list[i:j])

    return list_of_lists

def max_sum_subarray(my_list):
    list_of_lists=sublist_generator(my_list)
    max_sum=sum_list(list_of_lists[0])
    for lists in list_of_lists:
        if sum_list(lists)>=max_sum:
            max_sum=sum_list(lists)

    return max_sum

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = max_sum_subarray(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arr= [1, 2, 3, -4, 6]
solution= 8 # sum of array

test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, -5, -4, 1, 6]
solution = 7   # sum of last two elements

test_case = [arr, solution]
test_function(test_case)

arr = [-12, 15, -13, 14, -1, 2, 1, -5, 4]
solution = 18  # sum of subarray = [15, -13, 14, -1, 2, 1]

test_case = [arr, solution]
test_function(test_case)
