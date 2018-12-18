#(8, 9, 8)
def binary_search(arr, element, low, high):
	if low >= high:
		return False
	mid_index = (low + high)/2
	print(low, high, mid_index)
	if element == arr[mid_index]:
		return True
	elif element < arr[mid_index]:
		return (binary_search(arr, element, 0, mid_index - 1))
	elif element > arr[mid_index]:
		return(binary_search(arr, element, mid_index + 1, high))
	

if __name__ == '__main__':
	arr = map(int, raw_input('Enter array:\n').strip().split())
	element = int(raw_input('Enter element to find:\n'))
	if binary_search(arr, element, 0, len(arr)):
		print('Element is present')
	else:
		print('Element is not present')
