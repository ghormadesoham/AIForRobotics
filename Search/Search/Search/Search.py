#Lesson 4 Search 
# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# ----------

# 2 D list of checked elements
# 1 if checked

# returns a list
# in the form of [optimal path length, row, col].
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    path = []
    # create a copy of empty list--inefficent but okay for first implementation
    # review later 
    rows = len(grid)
    columns = len(grid[0])
    checked_elements  = [[False for _ in range(columns)] for _ in range(rows)]
    cost_matrix = [[0 for _ in range(columns)] for _ in range(rows)]
    open = []
    #[optimal path length, row, col]
    temp_var = [0, init[0], init[1]]
    open.append(temp_var)
    
    current = [0,0,0]
    #find the elements which are open (unchecked)
    #loop through the open elements
    while True:
        try:
            current = open.pop()
        except IndexError :
            return("fail")
            
        row_index = current[1];
        column_index = current[2];
        checked_elements[row_index][column_index] = True
        #print
        #print("Current element", grid[row_index][column_index])
        #print("Current element row",row_index)
        #print("Current element column",column_index)
        #print("Current element cost" ,current[0])
        #print("----------")
        
        if(current[1] == goal[0] and current[2] == goal[1]):
            break;

        
        temp_array = []
        #expand/find successors
        #expand the successor with the smallest cost first
        for d in range(len(delta)):              
            total_cost = current[0]
            r = row_index;
            c = column_index;
            #move to next cell
            r += delta[d][0];
            c += delta[d][1];
                
            #validity checks 
            #ignore negative values
            if(r < 0 or c < 0 or r > len(grid) - 1 or c > len(grid[0]) - 1):
                continue                
            if checked_elements[r][c]:
                continue

            # skip obstacles
            if(grid[r][c] == 1):
                continue
            
            # update the cost value for the element
            total_cost += cost;
            cost_matrix[r] [c] += total_cost;

            temp = [cost_matrix[r] [c], r, c]
            temp_array.append(temp)       
        
        # sort in descending order by cost 
        #use descending order to use pop method
        temp_array.sort(key = lambda x : x[0],reverse = True)
        for t in range(len(temp_array)):
            open.append(temp_array[t])
    
    path = [cost_matrix[row_index] [column_index], row_index ,column_index]
    #[optimal path length, row, col].
    return path

#Sebastian's solution with my code added for returning the expanded grid
def searchAndExpand(grid,init,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1

    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    
    x = init[0]
    y = init[1]
    g = 0

    open = [[g, x, y]]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand
    count = 0
    while not found and not resign:
        if len(open) == 0:
            resign = True
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            count +=1
            x = next[1]
            y = next[2]
            g = next[0]
            expand[x][y] += count
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
                            
    return expand

def searchAndPrintPath(grid,init,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1
    # cache the previous delta value
    action = [[ -1 for col in range(len(grid[0]))] for row in range(len(grid))]
    
    x = init[0]
    y = init[1]
    g = 0

    open = [[g, x, y]]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand
    
    while not found and not resign:
        if len(open) == 0:
            resign = True
            return 'fail'
        else:
            # sorting by g /cost here which is at the first index.         
            open.sort()
            open.reverse()
            next = open.pop()               
            
            x = next[1]
            y = next[2]
            g = next[0]
            # cache the element
                    
            
            if x == goal[0] and y == goal[1]:
                found = True
                
            else:
                for i in range(len(delta)):
                    #next position
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
                            # store the delta needed to get to this position from previous position
                            action[x2][y2] = i

    policy = [[ ' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    # traverse from goal to start/init
    x = goal[0]
    y = goal[1]
    policy[x][y] = '*'
    while x != init[0] or y != init[1]:
        #access the delta need to get to (x,y) location
        act = action[x][y]
        # previous position
        x2 = x - delta[act][0]
        y2 = y - delta[act][1]
        policy[x2][y2] = delta_name[act]
        # reset previous position as present position
        x = x2
        y = y2
    return policy # make sure you return the shortest path

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']
# test and print the final result
policy = searchAndPrintPath(grid,init,goal,cost)
for i in range(len(policy)):
    print(policy[i])
