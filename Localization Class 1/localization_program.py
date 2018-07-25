#determines where the robot is located.
def sense(p, Z, colors, sensor_right):
    #initialization
    q = []
    pHit = sensor_right;
    pMiss = 1 - sensor_right;
    #number of rows
    m = len(colors) 
    #number of columns
    n = len(colors[0])
    #sum 
    s = 0
    for i in range(m):
        temp = []
     
        for j in range(n):
            hit = (Z == colors[i][j]) 
            #product 
            temp.append(p[i][j] * (hit * pHit + (1-hit) * pMiss))
        q.append(temp)
        s = s + sum(temp) 
  
    #normalization
    if(s != 0):
        for i in range(m):
            for j in range(n):
                q[i][j] = q[i][j] / s
    return q

#moves the robot by U units.
def move(p, U, p_move, m, n):
    #initialization
    q = []
    pExact =  p_move;
    pUndershoot = 1 - p_move;#probability of staying at the same location
    
    for i in range(m):
        temp = []
     
        for j in range(n):
            s = pExact * p[(i - U[0])% m][(j - U[1])% n]
            #convolution /addition
            s = s + pUndershoot * p[i][j]
            temp.append(s)
        q.append(temp)

    return q

#p_move probablity that motion is correct
#sensor_right probability that the sensor is correct 
def localize(colors, measurements, motions, sensor_right, p_move):
    p = []
    #start with uniform distribution
    #number of rows
    m = len(colors) 
    #number of columns
    n = len(colors[0])
    #size 
    size = m * n;
  
    for i in range(m):
        temp = [];
        for j in range(n):
            temp.append(1/size);
        p.append(temp)
            

    for k in range(len(measurements)):
        p = move(p, motions[k], p_move, m, n)
        p = sense(p, measurements[k], colors, sensor_right)       

    return p