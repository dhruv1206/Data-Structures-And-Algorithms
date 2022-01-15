'''
🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳
'''

def sort_012(arr):

	starting=0
	ending=len(arr)-1
		
	current=0

	while current<=ending:
		if arr[current]==0:
			arr[current]=arr[starting]
			arr[starting]=0

			current+=1
			starting+=1

		elif arr[current]==2:
			arr[current]=arr[ending]
			arr[ending]=2

			ending-=1

		else:
			current+=1


	return arr


def test_function(test_case):
    test_case= sort_012(test_case)
    print(test_case)

    if test_case == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_case = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
test_function(test_case)

test_case = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
test_function(test_case)

test_case = [2, 2, 0, 0, 2, 1, 0, 2, 2, 1, 1, 1, 0, 1, 2, 0, 2, 0, 1]
test_function(test_case)

