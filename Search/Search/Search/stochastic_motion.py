# programming assignment lesson 4
# student notes:
# stochastic means non-deterministic /random
# i.e there is uncertainity in the motion
# deterministic motion happens when there is a 100 % chance of the motion
# we are using stochastic motion to program for clearances and tolerances so 
# we do not hit obstacles in the grid or fall off the grid
#
# --------------
# USER INSTRUCTIONS
#
# Write a function called stochastic_value that 
# returns two grids. The first grid, value, should 
# contain the computed value of each cell as shown 
# in the video. The second grid, policy, should 
# contain the optimum policy for each cell.
#
# --------------
# GRADING NOTES
#
# We will be calling your stochastic_value function
# with several different grids and different values
# of success_prob, collision_cost, and cost_step.
# In order to be marked correct, your function must
# RETURN (it does not have to print) two grids,
# value and policy.
#
# When grading your value grid, we will compare the
# value of each cell with the true value according
# to this model. If your answer for each cell
# is sufficiently close to the correct answer
# (within 0.001), you will be marked as correct.

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>'] # Use these when creating your policy grid.

# ---------------------------------------------
#  Modify the function stochastic_value below
# ---------------------------------------------

def stochastic_value(grid,goal,cost_step,collision_cost,success_prob):
    # Probability(stepping left) = prob(stepping right) = failure_prob

    failure_prob = (1.0 - success_prob)/2.0 
    # return these two 2-D lists
    value = [[collision_cost for col in range(len(grid[0]))] for row in range(len(grid))]
    policy = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
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
                            success = success_prob * value[x2][y2]
                            # left
                            index = (a + 1) % 4;
                            x_l = x + delta[index][0]
                            y_l = y + delta[index][1]
                            
                            # or falling off the grid ,or hitting obstacle
                            if not( x_l >= 0 and x_l < len(grid) and y_l >= 0 and y_l < len(grid[0]) and grid[x_l][y_l] == 0):
                                val = collision_cost
                            else:
                                val = value[x_l][y_l]

                            fail_left = failure_prob * val

                            # right
                            # modulo operation ensures that we do not
                            # 'fall' off i.e cycle from 0 to 3 and then back to 0
                            index = (a - 1) % len(delta);
                            x_r = x + delta[index][0]
                            y_r = y + delta[index][1]
                           
                            # or falling off the grid or collision into obstacle 
                            if  not (x_r >= 0 and x_r < len(grid) and y_r >= 0 and y_r < len(grid[0]) and grid[x_r][y_r] == 0):
                                val = collision_cost
                           
                            else:
                                val = value[x_r][y_r]

                            fail_right = failure_prob * val
                            v2 = success + fail_left + fail_right + cost_step
                            
                            
                            #update the value if it is less than 99(a high number)
                            if v2 < value[x][y]:
                                change = True
                                value[x][y] = v2
                                action[x][y] = a
   
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
        
    return value, policy

# ---------------------------------------------
#  Use the code below to test your solution
# ---------------------------------------------

grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]
#simple test case 1:no obstacles
#grid = [[0, 0, 0],
#        [0, 0, 0]]
#simple test case 2
#grid = [[0, 1, 0],
#        [0, 0, 0]]

goal = [0, len(grid[0])-1] # Goal is in top right corner
cost_step = 1
collision_cost = 100
success_prob = 0.5

# call method to test
value,policy = stochastic_value(grid,goal,cost_step,collision_cost,success_prob)
# print out the values
for row in value:
    print (row)
for row in policy:
    print (row)

# Expected outputs:
#
# [57.9029, 40.2784, 26.0665,  0.0000]
# [47.0547, 36.5722, 29.9937, 27.2698]
# [53.1715, 42.0228, 37.7755, 45.0916]
# [77.5858, 100.00, 100.00, 73.5458]
#
# ['>', 'v', 'v', '*']
# ['>', '>', '^', '<']
# ['>', '^', '^', '<']
# ['^', ' ', ' ', '^']

