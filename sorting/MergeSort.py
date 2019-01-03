#MergeSort

"""
Time complexity:- O(nlogn)
In order to analyze time complexity of merge sort first we must know about the
time complexity of merging of two sorted array of length n,into another sorted array
of length 2n, it comes out to be O (2 n).

Now in merge sort we are dividing array in two equal parts untill we get array of one
element, and again joining them in sorted order.

we will have to perform merging of array in all the levels with time complexity of O(n) (at each level),
for n elements we will have log (n) levels, and for each level we will perform n comparison
hence time complexity = O(nlogn)

"""

def mergesort(arr):

	if len(arr) > 1:
		mid = len(arr)//2
		left_part = arr[:mid]
		right_part = arr[mid:]

		mergesort(left_part) # Call recursively to divide array till length becomes 1
		mergesort(right_part)

		i = j = k = 0


		# Merge two parts of array
		while i < len(left_part) and j < len(right_part):
			if left_part[i] <= right_part[j]:
				arr[k] = left_part[i]
				i+=1
			else:
				arr[k] = right_part[j]
				j+=1
			k+=1

		while(i<len(left_part)):
			arr[k] = left_part[i]
			i+=1
			k+=1
		while(j<len(right_part)):
			arr[k] = right_part[j]
			j+=1
			k+=1

if __name__ == '__main__':
	array = map(int, raw_input('Enter your array:\n').strip().split())
	print('Your sorted array is:\n')
	mergesort(array)
	print(array)
	
