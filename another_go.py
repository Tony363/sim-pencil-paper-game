

drow = [0, -1, 0, 1]
dcolumn = [1, 0, -1, 0]


def bfs(board, i, j):
    rows = len(board)
    cols = len(board[0])

    queue = []
    queue.append([i, j])
    # print("i:{} j:{}".format(i, j))

    while queue.__len__() > 0:
        # print("first {}".format(queue[0]))
        a = queue[0][0]
        b = queue[0][1]

        queue.__delitem__(0)
        for k in range(0, 4):
            nrow = a + drow[k]
            ncolumn = b + dcolumn[k]

            if 0 <= nrow < rows and 0 <= ncolumn < cols and board[nrow][ncolumn] == '+':
                board[nrow][ncolumn] = board[i][j]
                queue.append([nrow, ncolumn])
    return board


def validate_board(board, n):
    msg = ""
    if not board:
        msg = "Board is empty."
        return False, msg

    row = len(board)
    if row != n:
        msg = "Board size doesn't match with input entered"
        return False, msg

    for r in board:
        # check if its square
        msg = "Board size doesn't match with input entered"
        if len(r) != n:
            return False, msg
        # check if consists of '+', 'X', 'O' chars
        for c in r:
            if c != '+' and c != 'X' and c != 'O':
                msg = "Board must consists only {}, {} and {}".format('+', 'X', 'O')
                return False, msg
    return True, msg


def print_board(board):
    for r in board:
        str_ = ""
        for c in r:
            str_ += c
        print(str_)

# This is where they score the board
def count_black_and_white(board):
    black = 0
    white = 0
    for row in board:
        for column in row:
            if column == 'X':
                black += 1
            if column == 'O':
                white += 1
    return black, white


def board_game():
    n = 0
    while True:
        try:
            n = int(input("Please enter a valid number of rows in the board: "))
            break
        except Exception as e:
            print("Please enter a valid number")

    board = []
    for i in range(0, n):
        print("Please enter {}th row. for e.g +XXOO++".format(i+1))
        row = str(input())
        board.append(list(row))
    success, msg = validate_board(board, n)
    if not success:
        print("Board is not valid. {}".format(msg))
        return

    print("We are scoring this board: ")
    print_board(board)

    for i in range(0, n):
        for j in range(0, n):
            if board[i][j] == 'X' or board[i][j] == 'O':
                bfs(board, i, j)

    print("Here is colored board: ")
    print_board(board)

    black, white = count_black_and_white(board)

    print("Black scored: {}".format(black))
    print("White scored: {}".format(white))


board_game()

