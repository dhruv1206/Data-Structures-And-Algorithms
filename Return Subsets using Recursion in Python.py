'''
🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳
'''

def subsets(arr):

    if len(arr) <= 1:
        return [arr]

    else:
        result=list()
        result.append(arr)
        for i in range(len(arr)):
            temp_arr=arr.copy()
            temp_arr.pop(i)
            result.extend(subsets(temp_arr))
        result_final=list()
        #This is to remove all duplicate cases
        for i , value in enumerate(result):
            if i == result.index(value):
                result_final.append(value)
            else:
                pass

        return result_final



def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = subsets(arr)

    output.sort()
    solution.sort()

    if output == solution:
        print("Pass")
    else:
        print("Fail")

arr = [9]
solution = [[9]]

test_case = [arr, solution]
test_function(test_case)

arr = [5, 7]
solution = [[7], [5], [5, 7]]
test_case = [arr, solution]
test_function(test_case)

arr = [9, 12, 15]
solution = [[15], [12], [12, 15], [9], [9, 15], [9, 12], [9, 12, 15]]

test_case = [arr, solution]
test_function(test_case)

arr = [9, 8, 9, 8]
solution = [[8],
[9],
[9, 8],
[8, 8],
[8, 9],
[8, 9, 8],
[9, 9],
[9, 9, 8],
[9, 8, 8],
[9, 8, 9],
[9, 8, 9, 8]]

test_case = [arr, solution]
test_function(test_case)
