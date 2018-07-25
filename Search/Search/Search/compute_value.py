# Dynamic Programming Lesson 4
# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 1, 0]]
#grid = [[0, 1, 0, 0, 0, 0],
#        [0, 1, 0, 0, 0, 0],
#        [0, 1, 0, 0, 0, 0],
#        [0, 1, 0, 0, 0, 0],
#        [0, 0, 0, 0, 1, 0]]
#grid = [[0, 0, 0, 0, 0, 0],
#        [0, 0, 1, 0, 0, 0],
#        [0, 0, 1, 0, 0, 0],
#        [0, 0, 0, 0, 1, 0],
#        [0, 0, 1, 1, 1, 0],
#        [0, 0, 0, 0, 1, 0]]

goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']
# Sebastian's solution
# I could not get one working for all grid cells:-/
def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    # f(x,y) = min f(x',y') + cost

    # 99 -a high value used to mark obstacles
    # all grid cells are obstacles by default
    value = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]
    # set change variable to True if any value in the value grid changes
    change = True
    while change == True:
        # set to false by default
        change = False
        # loop through grid cells
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                # if you reach goal cell
                if x == goal[0] and y == goal[1]:
                    if value[x][y] > 0:
                        value[x][y] = 0
                        change = True
                # all other cells
                elif grid[x][y] == 0 :
                    for i in range(len(delta)):
                        x2 = x + delta[i][0]
                        y2 = y + delta[i][1]
                        # check if x2 and y2 are within bounds 
                        if (x2 >= 0 and x2 < len(grid) 
                        and y2 >=0 and y2 < len(grid[0]) 
                        and grid[x2][y2] == 0):
                            v = value[x2][y2] + cost
                            if value[x][y] > v:
                                value[x][y] = v
                                change = True
                            

    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    return value 

def optimum_policy(grid,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    # cache the previous delta value
    action = [[ -100 for col in range(len(grid[0]))] for row in range(len(grid))]
    change = True

    while change:
        change = False

        # loop through all the grid cells
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                # for goal cell
                if goal[0] == x and goal[1] == y:
                    if value[x][y] > 0:
                        value[x][y] = 0
                        policy[x][y] = '*'

                        change = True

                elif grid[x][y] == 0:
                    for a in range(len(delta)):
                        x2 = x + delta[a][0]
                        y2 = y + delta[a][1]

                        # check whether the indices within bounds and 
                        # the grid cell is not an obstacle
                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                            v2 = value[x2][y2] + cost
                            
                            
                            #update the value if it is less than 99(a high number)
                            if v2 < value[x][y]:
                                change = True
                                value[x][y] = v2
                                action[x][y] = a
    policy = [[ ' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    # traverse from goal to start/init
    x = goal[0]
    y = goal[1]
    policy[x][y] = '*'
    for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]==0 and (x != goal[0] or y != goal[1]):
                    
                    #access the delta need to get to (x,y) location
                    if action[x][y] != -100:
                        act = action[x][y]
                        policy[x][y] = delta_name[act]
        
    return policy
# test and print the final result
result = optimum_policy(grid,goal,cost)
for i in range(len(result)):
    print(result[i])