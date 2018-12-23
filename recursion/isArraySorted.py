# Check if given array is sorted, using recursion.

def isArraySorted(array):
	if len(array) == 1: # Base condition
		return True
	return ((array[0] <= array[1]) and isArraySorted(array[1:])) # cursive condition

if __name__ == '__main__':
	array = map(int, raw_input('Enter array:\n').strip().split())
	if isArraySorted(array):
		print('Yes, given array is sorted')
	else:
		print('No, given array is not sorted')

