'''
🇮🇳🇮🇳🇮🇳 BY~DHRUV AGRAWAL , INDIA 🇮🇳🇮🇳🇮🇳
'''


def QuickSort(arr):
	if len(arr)<=1:
		return arr
	left=0
	pivot_index=len(arr)-1
	pivot_value=arr[pivot_index]
	while pivot_index!=left:
		item=arr[left]
		if item<=pivot_value:
			left+=1
			continue

		arr[left]=arr[pivot_index-1]
		arr[pivot_index-1]=arr[pivot_index]
		arr[pivot_index]=item
		pivot_index-=1
	arr[:pivot_index]=QuickSort(arr[:pivot_index])
	arr[pivot_index+1:]=QuickSort(arr[pivot_index+1:])
	return arr

print(QuickSort([96, 97, 98]))
	
