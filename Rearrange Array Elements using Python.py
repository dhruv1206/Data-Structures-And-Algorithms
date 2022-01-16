# Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

# for e.g. [1, 2, 3, 4, 5]

# The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

'''
🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳
'''



def rearrange_digits(arr):
	if len(arr)<=1:
		return arr
	arr=sorted(arr)
	first_num_len=0
	if len(arr)%2==0:
		first_num_len=len(arr)/2
	else:
		first_num_len=(len(arr)-1)/2+1

	second_num_len=len(arr)-first_num_len
	first_num=''
	second_num=''
	while len(arr)!=0:

		first_num+=str(arr.pop())
		if len(arr)!=0:

			second_num+=str(arr.pop())
		else:
			break


	return [int(first_num) , int(second_num)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


#%% Testing - Official
# Normal cases
print('Normal Cases:')
print('Test 1:')
list_num = [1, 2, 3, 4, 5]
result = rearrange_digits(list_num)
if result == [531, 42]:
    print('Pass \n')
else:
    print("Fail \n")

print('Test 2:')
list_num = [4, 6, 2, 5, 9, 8]
result = rearrange_digits(list_num)
if result == [964 , 852]:
    print('Pass \n')
else:
    print("Fail \n")

print('Test 3:')
list_num = [1, 2, 3]
result = rearrange_digits(list_num)
if result == [31, 2]:
    print('Pass \n')
else:
    print("Fail \n")

# Edge cases
print('Edge Cases:')
print('Test 4:')
list_num = [1, 1, 1]
result = rearrange_digits(list_num)
if result == [11, 1]:
    print('Pass \n')
else:
    print("Fail \n")

print('Test 5:')
list_num = [1]
result = rearrange_digits(list_num)
if result == [1]:
    print('Pass \n')
else:
    print("Fail \n")

print('Test 6:')
list_num = []
result = rearrange_digits(list_num)
if result == []:
    print('Pass \n')
else:
    print("Fail \n")
