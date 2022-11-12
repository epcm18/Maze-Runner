###############################################################################
################################      MAZE        #############################
###############################################################################

# took blocked sides as 1 and other sides as 0.

# virtical lines of each cell on each row
string1 = '''
100010010001001 110011000100011 000101011000101 111000100100111 111110001010011 
111111011101011 110111100111111 111111101110111 111011010111001 100010010001111 
111000101001111 101101011001100 110110011001011 100001000000001 '''

# horizontal lines of each cell on each row
string2 = '''
11111111111111 01010101011010 01110110011110 00101010111000 00001111101100 
00000110010110 00100010000001 10000001100000 00000001010100 01010110100010 
01111101110000 10011000011000 00000110110011 01101011011110 11111111111111 '''

maze = []
# make lists
v = string1.split()
h = string2.split()

# creating the maze as a matrix using v and h
for i in range(14):
    row = []
    for j in range(14):
        # take correct data from v and h for each cell 
        cell = [h[i][j], v[i][j+1], h[i+1][j], v[i][j]]
        row.append(cell)
    maze.append(row)
    
###############################################################################    
###############################################################################
    
def stuck(situation):
    """ to check the current cell is blocked by all sides"""
    if situation.count('1') == 4:
        return True
    return False

###############################################################################

# at starting position
path = ''
stack = [(2,0)]
i, j = stack[0]
print(f'Start at ( {i} , {j} )')

# going to maze
while True:
    # go out when current position is (11,13)
    if (i,j)==(11,13):
        # path for leave
        print(f'{path}Leaving at ( {i} , {j} )')
        break
    
    # sides of the current cell as N for North....
    N = maze[i][j][0]
    E = maze[i][j][1]
    S = maze[i][j][2]
    W = maze[i][j][3]

            
    if N == '0' :
        # block the side of North direction of the current cell 
        maze[i][j][0]='1'
        # add to path
        path +='North '
        # change the current location of the maze
        i -= 1
        maze[i][j][2]='1'
        # block the side of South direction of the current cell

        
    elif E == '0' :
        # block the side of East direction of the current cell 
        maze[i][j][1]='1'
        # add to path
        path +='East '
        # change the current location of the maze
        j += 1
        maze[i][j][3]='1'
        # block the side of West direction of the current cell
        
    elif S == '0' :
        # block the side of South direction of the current cell
        maze[i][j][2]='1'
        # add to path
        path +='South '
        # change the current location of the maze
        i += 1
        maze[i][j][0]='1'
        # block the side of North direction of the current cell
        
    elif W == '0':
        # block the side of West direction of the current cell
        maze[i][j][3]='1'
        # add to path
        path +='West '
        # change the current location of the maze
        j -= 1
        maze[i][j][1]='1'
        # block the side of East direction of the current cell

    # add coodinates to the stack
    stack.append((i,j))

    i,j = stack[-1]

    # all sides if current cell blocked is taken as stuck
    # then backtrack
    while stuck(maze[i][j]):
        # path to stuck location
        print(f'{path}Stuck at ( {i} , {j} )')
        # clear path
        path=''
        stack.pop(-1)
        # previous position (i,j)
        cp = stack[-1]
        i, j = cp[0], cp[1]
        # backtrack
        print(f'Back to ( {i} , {j} )')

###############################################################################