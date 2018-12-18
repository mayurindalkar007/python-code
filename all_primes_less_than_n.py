def do_marking(bool_arr, unmarked_num):
	i = 2
	index = i * unmarked_num
	while(index <= len(bool_arr)):
		bool_arr[index - 1] = True
		i += 1
		index = unmarked_num * i

	return bool_arr
		

def find_next_unmarked(bool_arr, unmarked):
	i = unmarked 
	while(i < len(bool_arr)):
		if not bool_arr[i]:
			return i + 1
		i += 1


if __name__ == '__main__':
	n = int(raw_input('Enter N i:\n'))
	bool_arr = [False] * n
	unmarked = 2
	while(unmarked < len(bool_arr)):
		if unmarked:
			do_marking(bool_arr, unmarked)
			unmarked = find_next_unmarked(bool_arr, unmarked)
		else:
			break


	for i in range(1, len(bool_arr)):
		if not bool_arr[i]:
			print(i+1)
