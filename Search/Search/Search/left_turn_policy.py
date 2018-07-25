# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's 
# optimal path to the position specified in goal; 
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a 
# right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']
cost = [2, 1, 20] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn
# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]



# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid,init,goal,cost):
    # 999 -a high value used to mark obstacles
    # all grid cells are obstacles by default
    
    # Orientation/theta is the third /new dimension which we need to 
    # account for.
    
    # there are four orientations possible -up ,left,down and right.
    # so store a mega grid comprising of 4 2-D grids for every orientation.
    # a mega grid is a list of 2-D lists.
    value = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))]]
    
    policy = [[[' ' for row in range(len(grid[0]))] for col in range(len(grid))],
              [[' ' for row in range(len(grid[0]))] for col in range(len(grid))],
              [[' ' for row in range(len(grid[0]))] for col in range(len(grid))],
              [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]]

    # the optimum policy in 2 dimensions
    # we need to output this variable.
    policy2D = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    
    # re-use code from previous exercise for optimum policy
    # but add new dimension
    change = True
    while change:
        change = False

        # loop through all the grid cells and all the orientations
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                for orientation in range(len(forward)):# length is 4-there are 4 orientations                    
                    # mark the goal cell
                    if goal[0] == x and goal[1] == y:
                        if value[orientation][x][y] > 0:
                            value[orientation][x][y] = 0
                            policy[orientation][x][y] ='*'
                            change = True
                    # for other non-obstacle cells... 
                    elif grid[x][y] == 0:
                        # loop through actions
                        for i in range(len(action)):#3 actions possible-R,#,L
                            # orientations are cyclic
                            orientation2 = (orientation + action[i]) % 4;
                            x2 = x + forward[orientation2][0]
                            y2 = y + forward[orientation2][1]
                                                 
                        # check whether the indices within bounds and 
                        # the grid cell is not an obstacle
                            if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                                # note that in this case the  if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0])
                                # cost varies depending on action                            
                                v2 = value[orientation2][x2][y2] + cost[i]                          
                            
                                #update the value if it is less than 999(a high number)
                                if v2 < value[orientation][x][y]:
                                    change = True
                                    value[orientation][x][y] = v2
                                    #memorize the action
                                    policy[orientation][x][y] = action_name[i]

    # initialization
    x = init[0]
    y = init[1]
    orientation = init[2]
    # convert 3-D policy into 2-D policy
    policy2D[x][y] = policy[orientation][x][y]

    # There are four motion directions: up, left, down, and right.
     # check whether or not you reached the goal
    while policy[orientation][x][y] != '*':
        # when you go straight orientation remains the same
        if policy[orientation][x][y] == '#':
            orientation2 = orientation
        # decreasing the index corresponds to making a 
        # right turn.   
        elif policy[orientation][x][y] == 'R':
            orientation2 = (orientation - 1) % 4
          # Increasing the index in this array corresponds to making a
          # a left turn
        elif policy[orientation][x][y] == 'L':
            orientation2 = (orientation + 1) % 4

        # update to new x,y,orientation
        x = x + forward[orientation2][0]
        y = y + forward[orientation2][1]
        orientation = orientation2
        policy2D[x][y] = policy[orientation][x][y]


    return policy2D

# print out the 2-D policy
result = optimum_policy2D(grid,init,goal,cost)
for i in range(len(result)):
    print(result[i])