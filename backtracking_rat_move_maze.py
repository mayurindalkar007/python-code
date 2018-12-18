def generate_path(maze, i, j, sol):
	sol[i][j] = 1
	if i == N - 1 and j == N - 1:
		return True

	if (i + 1 < N and maze[i+1][j] == 1):
		if generate_path(maze, i+1 , j, sol):
			return True
	if (j + 1 < N and maze[i][j + 1] == 1):
		if generate_path(maze, i , j+1, sol):
			return True
	sol[i][j] = 0
	return False


if __name__ == '__main__':
	N = int(raw_input("Enter value of N:\n"))
	maze = [[0] * N for i in range(N)]
	sol = [[0] * N for i in range(N)]
	print("Enter Maze:\n")
	for i in range(N):
		row = map(int, raw_input().strip().split())
		maze[i] = row[:]

	print("Your Maze:-\n")
	for i in range(N):
		str1 = ' '.join(str(x) for x in maze[i])
		print(str1)

	if generate_path(maze, 0, 0, sol):
		print("There exist a path:\n")
		for i in range(N):
			str1 = ' '.join(str(x) for x in sol[i])
			print(str1)
	else:
		print("No path exist")
	#print(maze)
		
