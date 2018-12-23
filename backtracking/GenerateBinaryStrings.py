def appendAtBignning(x, List):
	new_list = [x + element for element in List]
	return new_list
def bitString(n):
	if n == 0:
		return []
	if n ==1:
		return ['0', '1']
	else:
		return (appendAtBignning('0', bitString(n-1)) + appendAtBignning('1', bitString(n-1)))

if __name__ == '__main__':
	N = int(raw_input('Enter N to generate all all N bit binary strings:\n'))
	print(bitString(N))
