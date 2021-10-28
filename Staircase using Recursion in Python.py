'''
🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳
'''

def staircase(n):
    if n==0:
        return 1
    elif n<0:
        return 0

    else:
        result=0
        result+=staircase(n-1)
        result+=staircase(n-2)
        result+=staircase(n-3)
    return result

def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = staircase(n)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

n = 3
solution = 4
test_case = [n, solution]
test_function(test_case)
n = 4
solution = 7
test_case = [n, solution]
test_function(test_case)
n = 7
solution = 44
test_case = [n, solution]
test_function(test_case)
