from sys import maxint 

def find_current_max_sum(arr):
	"""This implimentation is using kadane's algo."""	
	max_so_far = -maxint - 1
	max_ending_here = 0
	up = 0
	down = 0
       
	for i in range(0, len(arr)): 
		max_ending_here = max_ending_here + arr[i] 
		if (max_so_far < max_ending_here): 
			max_so_far = max_ending_here
			up = i
			
  
		if max_ending_here < 0: 
			max_ending_here = 0
			down = i - up + 1 
	return max_so_far,up,down 

def find_max_sum_of_sub_2d_arr(matrix):
	L = 0
	R = 0
	current_sum = 0
	max_sum = 0
	max_left = 0
	max_right = 0
	max_up = 0
	max_down = 0
	print(len(matrix))
	#1d_arr = [0] * len(matrix)

	while(L < len(matrix[0])):
		d_arr = [0] * len(matrix)
		R = L
		while(R < len(matrix)):
			for i in range(len(d_arr)):
				d_arr[i] = d_arr[i] + matrix[R][i]
				curren_sum,up,down = find_current_max_sum(d_arr)
				if curren_sum > max_sum:
					max_sum = curren_sum
					max_left = L
					max_right = R
					max_up = up
					max_down = down
			R += 1
		L += 1

	return max_sum,max_left, max_right, max_up, max_down

if __name__ == '__main__':
	m,n = map(int, raw_input('Enter value for M and N for M X N matrix:\n').strip().split())
	print('Enter M X N matrix:\n')
	matrix = [[0]* n for i in range(m)]
        for i in range(m):
		arr_str = map(int, raw_input().strip().split())
		matrix[i] = arr_str[:]
	print('Your matrix is:\n')
	for i in range(m):
		print(matrix[i])

	max_sum,max_left, max_right, max_up, max_down = find_max_sum_of_sub_2d_arr(matrix)

	print('Your max sum is-->')
	print(max_sum, max_left, max_right, max_up, max_down)
	print('Your sub-array is-->')

	for i in range(max_down, max_up+1):
		print(matrix[i][max_left:max_right+1])
