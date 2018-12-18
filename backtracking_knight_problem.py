def knight_moves(board, N, i , j):
    if N == 0:
        board[i][j] = 1
        return 1
    else:
        if i - 2 >= 0 and j + 1 < 10:
            knight_moves(board, N-1, i-2 , j+1)
        if i - 2 >= 0 and j - 1 >= 0:
            knight_moves(board, N-1, i-2 , j-1)
        if i + 2 < 10 and j + 1 < 10:
            knight_moves(board, N-1, i+2 , j+1)
        if i + 2 < 10 and j - 1 >= 0:
            knight_moves(board, N-1, i+2 , j-1)
        if i - 1 >= 0 and j + 2 < 10:
            knight_moves(board, N-1, i-1 , j+2)
        if i - 1 >= 0 and j - 2 >= 0:
            knight_moves(board, N-1, i-1 , j-2)
        if i + 1 < 10 and j + 2 < 10:
            knight_moves(board, N-1, i+1 , j+2)
        if i + 1 < 10 and j - 2 >= 0:
            knight_moves(board, N-1, i+1 , j-2)
    
    

if __name__ == '__main__':
    N = map(int, raw_input("Enter current position and number of moves\n").strip().split())
    print(N)
    board = [[0]*10 for i in range(10)]
    for i in range(10):
        print(' '.join(str(x) for x in board[i]))
 
    print("=============================================")
    knight_moves(board, N[2], N[0] -1, N[1] - 1)
    for i in range(10):
        print(' '.join(str(x) for x in board[i]))
    count = 0
    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                #print("i,j=======>",i,j)
                count += 1
    print(count)
