'''
🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳
'''


def HeapSort(arr):
	for i in range(len(arr)):
		arr=Heapify(i ,arr)

	replacer=len(arr)-1
	for i in range(len(arr)-1):
		max_value=arr[0]
		arr[0] , arr[replacer]=arr[replacer] , max_value

		for i in range(replacer):
			arr=Heapify(i , arr)
		replacer-=1
	return arr





def Heapify(index , arr):
	if  index==0:
		return arr

	
	parent_index=(index-1)//2
	parent_value=arr[parent_index]
	children_value=arr[index]

	if children_value>parent_value:
		arr[parent_index] , arr[index] = children_value  , parent_value
		arr=Heapify(parent_index , arr)
	else:
		pass

	return arr


def test_function(test_case):
    HeapSort(test_case[0])
    if test_case[0] == test_case[1]:
        print("Pass")
    else:
        print("False")


arr = [3, 7, 4, 6, 1, 0, 9, 8, 9, 4, 3, 5]
solution = [0, 1, 3, 3, 4, 4, 5, 6, 7, 8, 9, 9]

test_case = [arr, solution]

test_function(test_case)

arr = [5, 5, 5, 3, 3, 3, 4, 4, 4, 4]
solution = [3, 3, 3, 4, 4, 4, 4, 5, 5, 5]
test_case = [arr, solution]
test_function(test_case)

arr = [99]
solution = [99]
test_case = [arr, solution]
test_function(test_case)

arr = [0, 1, 2, 5, 12, 21, 0]
solution = [0, 0, 1, 2, 5, 12, 21]
test_case = [arr, solution]
test_function(test_case)
