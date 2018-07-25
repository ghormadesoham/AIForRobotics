#[0, 0]  no work
#[0, 1]  move right 
#[0,-1]  move left
#[1, 0]  move down 
#[0,-1]  move up 


from localization_program import localize
from localization_program import move
from operator import sub
import numpy as np 

colors = [['G', 'G', 'G'],
          ['G', 'R', 'G'],
          ['G', 'G', 'G']]
#number of rows
m = len(colors) 
#number of columns
n = len(colors[0])
# test 1
##red
#measurements = ['R']
##no movement
#motions = [[0,0]]
#sensor_right = 1.0
#p_move = 1.0
#p = localize(colors,measurements,motions,sensor_right,p_move)

#correct_answer = (
#    [[0.0, 0.0, 0.0],
#     [0.0, 1.0, 0.0],
#     [0.0, 0.0, 0.0]])
#print("Test 1")
#print(p)
#print(correct_answer)

## test 2
#colors = [['G', 'G', 'G'],
#          ['G', 'R', 'R'],
#          ['G', 'G', 'G']]
#measurements = ['R']
#motions = [[0,0]]
#sensor_right = 1.0
#p_move = 1.0
#p = localize(colors,measurements,motions,sensor_right,p_move)
#correct_answer = (
#    [[0.0, 0.0, 0.0],
#     [0.0, 0.5, 0.5],
#     [0.0, 0.0, 0.0]])
#print("Test 2")
#print(p)

## test 3
#colors = [['G', 'G', 'G'],
#          ['G', 'R', 'R'],
#          ['G', 'G', 'G']]
#measurements = ['R']
#motions = [[0,0]]
#sensor_right = 0.8
#p_move = 1.0
#p = localize(colors,measurements,motions,sensor_right,p_move)
#correct_answer = (
#    [[0.06666666666, 0.06666666666, 0.06666666666],
#     [0.06666666666, 0.26666666666, 0.26666666666],
#     [0.06666666666, 0.06666666666, 0.06666666666]])
#print("Test 3")
#print(p)
#print(correct_answer)

## test 4
#colors = [['G', 'G', 'G'],
#          ['G', 'R', 'R'],
#          ['G', 'G', 'G']]
#measurements = ['R', 'R']
## no movement , move right 
#motions = [[0,0], [0,1]]
#sensor_right = 0.8
#p_move = 1.0
#p = localize(colors,measurements,motions,sensor_right,p_move)
#correct_answer = (
#    [[0.03333333333, 0.03333333333, 0.03333333333],
#     [0.13333333333, 0.13333333333, 0.53333333333],
#     [0.03333333333, 0.03333333333, 0.03333333333]])
#print("Test 4")
#print(p)
#print(correct_answer)

#test 5
#colors = [['G', 'G', 'G'],
#          ['G', 'R', 'R'],
#          ['G', 'G', 'G']]
#measurements = ['R', 'R']
#motions = [[0,0], [0,1]]
#sensor_right = 1.0
#p_move = 1.0
#p = localize(colors,measurements,motions,sensor_right,p_move)
#correct_answer = (
#    [[0.0, 0.0, 0.0],
#     [0.0, 0.0, 1.0],
#     [0.0, 0.0, 0.0]])
#print("Test 5")
#print(p)
#print(correct_answer)

#test 6
#colors = [['G', 'G', 'G'],
#          ['G', 'R', 'R'],
#          ['G', 'G', 'G']]
#measurements = ['R', 'R']
#motions = [[0,0], [0,1]]
#sensor_right = 0.8
#p_move = 0.5
#p = localize(colors,measurements,motions,sensor_right,p_move)
#correct_answer = (
#    [[0.0289855072, 0.0289855072, 0.0289855072],
#     [0.0724637681, 0.2898550724, 0.4637681159],
#     [0.0289855072, 0.0289855072, 0.0289855072]])

#print("Test 6")
#print(p)
#print(correct_answer)


## test 7
colors = [['G', 'G', 'G'],
          ['G', 'R', 'R'],
          ['G', 'G', 'G']]
measurements = ['R', 'R']
motions = [[0,0], [0,1]]
sensor_right = 1.0
p_move = 0.5
p = localize(colors,measurements,motions,sensor_right,p_move)
correct_answer = (
    [[0.0, 0.0, 0.0],
     [0.0, 0.33333333, 0.66666666],
     [0.0, 0.0, 0.0]])
print("Test 7")
print(p)
print(correct_answer)



tol_matrix = [];
#set up tolerance matrix
for i in range(m):
    temp = []
    for j in range(n):
        temp.append(0.01)#tolerenace
    tol_matrix.append(temp)
  
#Verify solution 
A = np.array(p)
B = np.array(correct_answer)
tol = np.array(tol_matrix)
C = A - B
result = abs(C) < tol
if(result.all() == True):
    print("Nice Work!")
else:
    print("try again!")


#measurements = ['R']
##no movement
#motions = [[0,0]]
#sensor_right = 1.0
#p_move = 1.0
##test move()
#p = [0]
#size= m * n;
#for i in range(m):
#    temp = [];
#    for j in range(n):
#        temp.append(1/size);
#    p.append(temp)
#print(p)
#U = [0,0]
#p = move(p, U, p_move, m, n)

#print(p)