
game = open(input('What is the filename?:'), "r")
gameboard = game.read()
game.close()
print(gameboard)

# import sys
# with open(sys.argv[1], 'r') as f:
#     contents = f.read()
# print(contents)