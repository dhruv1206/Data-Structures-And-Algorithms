'''
🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳
'''


def sqrt(num):
	if num<0:
		return None

	elif num==0 or num==1:
			return num
	
	start=0
	end=num//2
	result=0
	while start<=end:
		middle=(start+end)//2

		if middle*middle==num:
			return middle

		elif middle*middle<num:
			start=middle+1 
			result=middle

		else:
			end=middle-1

	return result


print('Normal Cases:')
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass \n" if (5 == sqrt(27)) else "Fail \n")

# Edge cases
print('Edge Cases:')
print("Pass" if (None == sqrt(-1)) else "Fail")
print("Pass" if (99380 == sqrt(9876543210)) else "Fail")
print(sqrt(1234567890987654321234567890))
