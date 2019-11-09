
from proj2_ui import print_board
#I decided to called this pick_color because i tested this with 2 color importing rhino
#Instead in this project i will use characters
#
def pick_colors():
    valid_picks = False
    while not valid_picks:
        player_1 = input('Hello, what character would player 1 like to use?')
        player_2 = input('Hello, what character would player 2 like to use?')
        valid_picks = player_1 != player_2
        if not valid_picks:
            print("Error. Both players have same character")
    return player_1, player_2


def check_move(move, player_lines):
    #Check the move at indexes since we have 6 dots the move will be between 1 to 6 inclusively.
    if not 1 <= move[0] <= 6:#check player1 move in range 1 to 6 
        return "Invalid Move. Point 1 should be between 1 and 6"
    elif not 1 <= move[1] <= 6:#check player2 move in range 1 to 6
        return "Invalid Move. Point 2 should be between 1 and 6"
    elif move[0] == move[1]:# A line cannot be reflexive
        return "Invalid Move. A line cannot be drawn from one dot to itself."
    elif move in player_lines[0] or move in player_lines[1]:#cannot input 1 2  and 2  1 
        return "Invalid Move. A line cannot be drawn over an existing line."
    return None #Nonetype return none if the above condition are not stisfied 


def accept_player_move(player):
    valid_line = False
    while not valid_line:
        line = input("Enter a line for player {}:".format(player))
        points = line.split()
        valid_line = len(points) == 2
        if valid_line:
            point1, point2 = int(points[0]), int(points[1])
        else:
            print("Error. Please enter both row and column separated by a space")
            #press tab to keep space while inputing row and column
    if point2 < point1:
        point1, point2 = point2, point1
    return point1, point2


def check_triangle(player_lines):
    #this function will check player lines 
    #if the the move form a triangle of different character the game will continue 
    #if the move form a triangle of with a unique character the it will return true
    #it will be called by take_turn() then return the loser
    if not player_lines:
        return False

    last_line = player_lines[-1]
    other_lines = player_lines[:-1]
    dot1, dot2 = last_line
    for i in range(1,7):
        if ((dot1, i) in other_lines or (i, dot1) in other_lines) and  ((dot2, i) in other_lines or (i, dot2) in other_lines):
            return True


def play_game():
    players = pick_colors()
    #empty list to store player move
    player_lines = [[],[]]
    current_player = 1
    game_over = False
    while not game_over:
        #!game_over function takes three parameters the current player, the player_lines and players(player1 and player2)
        #this control the game flow
        #while not game over the turn will turn flow will take control and the next player will play
        #else print game over p1 or p2 loses
        game_over = take_turn(current_player, player_lines, players)
        if not game_over:
            current_player = 3 - current_player
    print_board(player_lines[0], players[0], player_lines[1], players[1])
    print("Game over. player {} loses.".format(current_player))


def take_turn(current_player, player_lines, players):
    #take_turn(current_player, player_lines, players)
    #this function will control the turn flow
    #call print_board
    #call accept_player_move
    #
    print_board(player_lines[0], players[0], player_lines[1], players[1])
    move = accept_player_move(current_player)
    move_error = check_move(move, player_lines)
    while move_error:
        print(move_error)
        move = accept_player_move(current_player)
        move_error = check_move(move, player_lines)
    player_lines[current_player - 1].append(move)
    game_over = check_triangle(player_lines[current_player - 1]) #here game_over is set to check_triangle
    return game_over#if one player draw a monochromatic triangle that player lose the game 


if __name__ == "__main__":
    play_game()
    #checking if all all function are working
    #pick_colors()
    #accept_player_move(1)
    #print(check_move([1,2],[[[1,2]],[]]))
    #print(check_move([1, 1], [[[1, 2]], []]))
    #print(check_move([7, 1], [[[1, 2]], []]))
    #print(check_move([1, 7], [[[1, 2]], []]))
    #print(check_triangle([(1, 2), (2, 4), (1, 4)]))
    #print(check_triangle([(1, 3), (2, 4), (1, 4)]))
