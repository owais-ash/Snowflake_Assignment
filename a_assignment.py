def solve(board):
    if not board:
        return []

    n, m = len(board), len(board[0])

    def dfs(i, j):
        if i < 0 or i >= n or j < 0 or j >= m or board[i][j] != 'O':
            return
        board[i][j] = 'k'  
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)

    for i in range(n):
        dfs(i, 0)
        dfs(i, m-1)
    for j in range(m):
        dfs(0, j)
        dfs(n-1, j)

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'k':
                board[i][j] = 'O'

    return board

n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))

board = []
print("Enter each row of the board, with cells separated by space (use 'X' or 'O'):")
for _ in range(n):
    row = input().split()[:m]  
    board.append(row)

      
solved_board = solve(board)
print("Solved board:- ")
for row in solved_board:
    print(' '.join(row))
