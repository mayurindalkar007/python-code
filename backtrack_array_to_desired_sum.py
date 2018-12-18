sum_list = []
desired_sum_length = [0, 0, 0]
final_combination = []
count = 0
def desired_sum(arr, sum_till_now, str1, i):
	if sum_till_now == desired_sum_length[0]:
		final_combination.append(str1.strip())
		desired_sum_length[2] += 1
		return
	if i == desired_sum_length[1] or sum_till_now > desired_sum_length[0]:
		return
	desired_sum(arr, sum_till_now, str1, i+1)
	str1 = str1 + " " + str(arr[i])
	desired_sum(arr, sum_till_now + arr[i], str1, i+1)
        
	
if __name__ == '__main__':
	arr = map(int, raw_input("Enter your array, space seperated\n").strip().split())
	desired_sum_length[0] = int(raw_input("Enter your desired sum\n"))

        desired_sum_length[1] = len(arr)
	desired_sum(arr, 0, '', 0)	
	print("Your combinations:-\n")
	print(final_combination)
	print(desired_sum_length[2])
