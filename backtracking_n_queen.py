def is_attacked(i, j, board):
	length = len(board[0])
	for k in range(0, length):
		if board[i][k] == 1:
			return True
	for k in range(0, length):
		if board[k][j] == 1:
			return True
	m = i
	n = j
	while(m >=0 and n < length):
		if board[m][n] == 1:
			return True
		m -= 1
		n += 1
	m = i
	n = j
	while(m < length and n >= 0):
		if board[m][n] == 1:
			return True
		m += 1
		n -= 1

	m = i
	n = j
	while(m < length and n < length):
		if board[m][n] == 1:
			return True
		m += 1
		n += 1

	m = i
	n = j
	while(m >=0 and n >= 0):
		if board[m][n] == 1:
			return True
		m -= 1
		n -= 1

	return False

def is_n_queen(board, N, length):
	if N == 0:
		return True	
	for i in range(0, length):
		for j in range(0, length):
			if is_attacked(i, j, board):
				continue
			board[i][j] = 1
			if is_n_queen(board, (N-1), length):
				return True
			board[i][j] = 0 
	return False

if __name__ == '__main__':
	N = int(input("Enter value of N:\n"))
	board = [[0]*N for i in range(N)]
	length = len(board[0])
	if is_n_queen(board, N, length):
		print("Yes can placed N queens")
		for i in range(length):
			print(board[i])
	else:
		print("Cannot place N queens")
