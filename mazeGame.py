#### Maze Runner 2D
### Move Around The Maze To Escape
## By: Dane Folk
# 21 December 2022


import sys, os

### Maze File Constraints ###
WALL = '#'
EMPTY = ' '
START = 'S'
EXIT = 'E'

PLAYER = '@'
BLOCK = chr(9617)

def displayMaze(maze):
    
    ### Maze Display ###

    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x,y) == (playerx,playery):
                print(PLAYER, end="")
            elif (x,y) == (exitx, exity):
                print('X', end="")
            elif maze [(x,y)] == WALL:
                print (BLOCK, end="")
            else:
                print (maze[(x,y)], end ="")
      
        ###New line after printing row ###
        print() 
    
print ("Maze Runner 2D")

### Get file name from the user ###

while True:
    print('Enter The Filename of the maze (or LIST or QUIT):')
    filename = input('> ')

    ### List all the maze files in the current folder ###

    if filename.upper() == ('LIST'):
        print ('Maze Files Found In', os.getcwd())
        for fileInCurrentFolder in os.listdir():
            if (fileInCurrentFolder.startswith('maze') and fileInCurrentFolder.endswith('.txt')):
                print (' ', fileInCurrentFolder)
        continue

    if filename.upper() == ('QUIT'):
        sys.exit()

    if os.path.exists(filename):
        break
    print('No File Named', filename)


### Load The Maze From A File ###

mazeFile = open(filename)
maze = {}
lines = mazeFile.readlines()
playerx = None
playery = None
exitx = None
exity = None
y = 0
for line in lines:
    WIDTH = len(line.rstrip())
    for x, character in enumerate(line.rstrip()):
        assert character in (WALL, EMPTY, START, EXIT), 'Invalid character at column {}, line {}'.format(x+1, y+1)
        if character in (WALL, EMPTY):
            maze[(x,y)] = character
        elif character == START:
            playerx, playery = x, y
            maze [(x,y)] = EMPTY
        elif character == EXIT:
            exitx, exity = x, y
            maze [(x,y)] = EMPTY
    y += 1
HEIGHT = y

assert playerx != None and playery != None, 'No start in the Maze File'
assert exitx != None and exity != None, 'No exit in the Maze File'

### Main Game Loop ###

while True:
    displayMaze(maze)

    ### Get User Move ###
    while True:
        print('                            W')
        print('Enter directions or QUIT : ASD')
        move = input('> ').upper()

        if move == 'QUIT':
            print ('Thanks for playing!')
            sys.exit()

        if move not in ['W', 'A', 'S', 'D']:
            print ('Invalid Directions: Move with W A S D')
            continue

        ### Check if Player Can Move ###

        if move == 'W' and maze[(playerx, playery - 1)] == EMPTY:
            break
        elif move == 'S' and maze[(playerx, playery + 1)] == EMPTY:
            break
        elif move == 'A' and maze[(playerx - 1, playery)] == EMPTY:
            break
        elif move == 'D' and maze[(playerx + 1, playery)] == EMPTY:
            break

        print ('There is a wall there!')

    ### Keep Moving Until You Encounter A Break Point ###

    if move == 'W':
        while True:
            playery -= 1
            if (playerx, playery) == (exitx, exity):
                break
            if maze[(playerx, playery - 1)] == WALL:
                ### If a wall is hit ###
                break
            if (maze[(playerx - 1, playery)] == EMPTY or maze[(playerx + 1, playery)] == EMPTY):
                ### Break Point Reached ###
                break

    elif move == 'S':
        while True:
            playery += 1
            if (playerx, playery) == (exitx, exity):
                break
            if maze[(playerx, playery + 1)] == WALL:
                ### If a wall is hit ###
                break
            if (maze[(playerx - 1, playery)] == EMPTY or maze[(playerx + 1, playery)] == EMPTY):
                ### Break Point Reached ###
                break

    elif move == 'A':
        while True:
            playerx -= 1
            if (playerx, playery) == (exitx, exity):
                break
            if maze[(playerx - 1, playery)] == WALL:
                ### If a wall is hit ###
                break
            if (maze[(playerx, playery - 1)] == EMPTY or maze[(playerx, playery + 1)] == EMPTY):
                ### Break Point Reached ###
                break

    elif move == 'D':
        while True:
            playerx += 1
            if (playerx, playery) == (exitx, exity):
                break
            if maze[(playerx + 1, playery)] == WALL:
                ### If a wall is hit ###
                break
            if (maze[(playerx, playery - 1)] == EMPTY or maze[(playerx, playery + 1)] == EMPTY):
                ### Break Point Reached ###
                break
    
    if (playerx, playery) == (exitx, exity):
        displayMaze(maze)
        print('You Have Reached The Exit! Congrats!')
        print('Thanks For Playing!')
        sys.exit()

