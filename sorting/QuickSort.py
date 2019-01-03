# Quick sort
"""
Time complexity:
	Worst Case = O(n-square)
	Average Case = O(nlogn)
	Best Case = O(nlogn)
"""

def partition(arr, low, high):
	pivot_ele = arr[high]
	index = low
	for j in range(low, high):
		if arr[j] <= pivot_ele:
			arr[j], arr[index] = arr[index], arr[j]
			index += 1

	arr[high], arr[index] = arr[index], arr[high]
	return index

def quicksort(arr, low, high):
	if (low < high):
		pivot = partition(arr, low, high)
		print(arr)
		quicksort(arr, low, pivot-1)
		quicksort(arr, pivot+1, high)

if __name__ == '__main__':
	array = map(int, raw_input('Enter array:-\n').strip().split())

	quicksort(array, 0, len(array) - 1)
	print('Your sorted array:-\n')
	print(array)
