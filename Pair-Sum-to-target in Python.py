'''
🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳
'''

def pair_sum_to_zero(input_list , target):
	dictionary=dict()
	for index , value in enumerate(input_list):
		if target-value in dictionary:
			return [dictionary[target-value] , index]
		dictionary[value]=index

def test_function(test_case):
    output = pair_sum_to_zero(test_case[0], test_case[1])
    print(output)
    if sorted(output) == test_case[2]:
        print("Pass")
    else:
        print("Fail")

test_case_1 = [[1, 5, 9, 7], 8, [0, 3]]
test_function(test_case_1)

test_case_2 = [[10, 5, 9, 8, 12, 1, 16, 6], 16, [0, 7]]
test_function(test_case_2)
