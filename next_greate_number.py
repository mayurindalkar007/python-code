
def next_greater_num(num):
	str1 = str(num)
	list1 = map(int, list(str1))
	#print(list1)
	for i in range(len(list1)-1, -1, -1):
		#print('i-->', list1[i])
		found = False
		for j in range(i+1, len(list1)):
			#print('j -->', list1[j])
			next_max = max(list1[i+1:])
			#print('next_max ' , next_max)
			tmp = list1[j]
			if tmp > list1[i] and tmp <= next_max:
				#print('in if')
				next_max = tmp
				next_index = j
				#print('next_index ', next_index)
				found = True

		if found:
			list1[i], list1[next_index] = list1[next_index], list1[i]
			#print(list1)
			final_list = list1[:i+1] + sorted(list1[i+1:])
			return ''.join(map(str, final_list))

if __name__ == '__main__':

	number = raw_input('Enter your number:\n')
	print('Next greater number is :')
	print(next_greater_num(number))
