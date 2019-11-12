import sys
import random
# matrix = [
#    [1,2],
#     [3,4],
#     [5,6],
#  ]
# tony = [[row[i] for row in matrix] for i in range(2)]
# print(tony)
# points = random.sample([range(1,7),range(1,7)],3)
# print(points)
#losing_condtion= [[x,y],[y,z],[z,x]]
losing_condition = [
    [[x,y] for x in range(1,7) for y in range(1,7)],
    [[y,z] for y in range(1,7) for z in range(1,7)],
    [[z,x] for z in range(1,7) for x in range(1,7)]
]
print(losing_condition)

def choice_character(*args):
    player_1 = input('Enter your character:')
    player_2 = input('Enter your character:')
    if player_1 == player_2:
        sys.exit(1)
    return player_1,player_2

player_1_moves = []
def player_move():
    
    while True:
        first_value = int(input())
        second_value = int(input())
        player_move = {first_value,second_value}
        if first_value > 6 or second_value < 1:
            break
        elif second_value > 6 or second_value < 1:
            break
     
        elif (len(player_move)> 2):
            break
        
        for move in player_1_moves:
            if player_move == move:
                break
        player_1_moves.append(player_move)   

print(player_1_moves)     
player_move()

print(choice_character())


# player_2_moves = [player_move() for player_move in range(15)]



print('Moves of player 1:',player_1_moves)
# print('Moves of player 2:',player_2_moves)

for move in player_1_moves:
    organized_move = move.sort()
for side in losing_condition:
    for vertices in side:
        organized_vertices = vertices.sort()

if organized_move == organized_vertices:
    print(organized_move, organized_vertices)
    



