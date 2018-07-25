# Lesson 4 Search with A*
# -----------
# User Instructions:
#
# Modify the the search function so that it becomes
# an A* search algorithm as defined in the previous
# lectures.
#
# Your function should return the expanded grid
# which shows, for each element, the count when
# it was expanded or -1 if the element was never expanded.
# 
# If there is no path from init to goal,
# the function should return the string 'fail'
# ----------
# student notes:
# see lesson 4 Q and A
# there are alternatives to A*  and so it not the only option
# the heuristic function for Stanford's Junior is computed in two ways:
# 1. solving as the plabnning problem as a 2-D problem i.e w/o rotation
# 2. solving the 3-D planning problem w/o obstacles
# for 1. 2-D planning is faster than 3-D so this works.
# we combine 1 and 2 to generate the heuristic

# we can have multiple goals
# Junior maps to the visual horizon i.e it does not
# plan to a goal but only to what it can see
# Junior does not react to audible noises 
# such as honks from other cars 
#
# admissible heuristic :
# under-estimating the goal 
 #i.e h(x) <= cost to goal 
grid = [[0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0]]
# each value defines the number of steps needed to reach the goal.
# for cars,we use euclidean distance instead of steps
heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]
# A* w/o heuristic (commment out line below) is plain search
#  a plain search will expand nodes away from the goal
# whereas A* will only expand nodes which bring us closer to the goal.
# so A* is more efficient than a plain search algorithm.
#heuristic = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost,heuristic):
    # ----------------------------------------
    # modify the code below
    # ----------------------------------------
    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed[init[0]][init[1]] = 1

    expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    action = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]

    x = init[0]
    y = init[1]
    g = 0
    h = heuristic[x][y]
    # f = g + h(x,y)
    f = g + h

    open = [[f, g, x, y]]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand
    count = 0
    
    while not found and not resign:
        if len(open) == 0:
            resign = True
            return "Fail"
        else:
            # sorting by f value here which is at the first index.
            # we can sort by other indices as well but simpler to move the 
            # index of interest to first position
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[2]
            y = next[3]
            g = next[1]
            f = next[0]
            expand[x][y] = count
            count += 1
            
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            h2 = heuristic[x2][y2]
                            f2 = g2 + h2

                            open.append([f2, g2, x2, y2])
                            closed[x2][y2] = 1

    return expand
# test and print the final result
expand = search(grid,init,goal,cost,heuristic)
for i in range(len(expand)):
    print(expand[i])