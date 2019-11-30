A = []
with open(str(input()), 'r') as f:
    for line in f:
        A.append(list(line.split()))
print(A)
# check for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]: 


# def moveLeft(i,j,owner,board):
#     if board[i][j]=='+' and i>=0 and i<=len(board) and j>=0 and j<=len(board[0]) :
#         colorBoard('left',i,j,len(board),len(board[0]),owner,board)

# def moveRight(i,j,owner,board):
#     if board[i][j]=='+' and i>=0 and i<=len(board) and j>=0 and j<=len(board[0]) :
#         colorBoard('right',i,j,len(board),len(board[0]),owner,board)

# def moveUp(i,j,owner,board):
#     if board[i][j]=='+' and i>=0 and i<=len(board) and j>=0 and j<=len(board[0]) :
#         colorBoard('up',i,j,len(board),len(board[0]),owner,board)

# def moveDown(i,j,owner,board):
#     if board[i][j]=='+' and i>=0 and i<=len(board) and j>=0 and j<=len(board[0]) :
#         colorBoard('down',i,j,len(board),len(board[0]),owner,board)

# def colorBoard(direction,i,j,m,n,owner,board):
#     if i>=0 and i<=n and j>=0 and j<=m:
#         return board[i][j]=owner
#     if direction=='left':
    
#         colorBoard(direction,i,j-1,m,n,owner,board)
#     if direction=='right':
#         colorBoard(direction,i,j+1,m,n,owner,board)
#     if direction=='up':
#         colorBoard(direction,i-1,j,m,n,owner,board)
#     if direction=='down':
#         colorBoard(direction,i+1,j,m,n,owner,board)
#     for i in range(len(board)):
#         for j in range(len(board[i])):
  
#             if board[i][j]=='X' or board[i][j]=='O':
#                 moveLeft(i,j-1,board[i][j],board)
#                 moveRight(i,j+1,board[i][j],board)
#                 moveUp(i-1,j,board[i][j],board)
#                 moveDown(i+1,j,board[i][j],board)
        
    
# print(board)