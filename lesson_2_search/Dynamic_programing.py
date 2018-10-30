
# coding: utf-8

# In[1]:

def optimum_policy2D(grid,init,goal,cost):
    value = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
             [[999 for row in range(len(grid[0]))] for col in range(len(grid))]]

    policy = [[[' ' for row in range(len(grid[0]))] for col in range(len(grid))],
             [[' ' for row in range(len(grid[0]))] for col in range(len(grid))],
             [[' ' for row in range(len(grid[0]))] for col in range(len(grid))],
             [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]]

    policy2D = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

    change = True
    while change:
        change = False
        #go through all grid cells and calculate values
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                for orientation in range(4):
                    if goal[0]==x and goal[1]==y:
                        if value[orientation][x][y]>0:
                            change = True
                            value[orientation][x][y] = 0
                            policy[orientation][x][y] = '*'
                    elif grid[x][y]==0:
                        for i in range(len(action)):
                            o2 = (orientation+action[i])%4
                            x2 = x+forward[o2][0]
                            y2 = y+forward[o2][1]

                            if x2>=0 and x2< len(grid) and y2>=0 and y2<len(grid[0]) and grid[x2][y2]==0:
                                v2 = value[o2][x2][y2]+cost[i]
                                if v2 < value[orientation][x][y]:
                                    value[orientation][x][y] = v2
                                    change = True
                                    policy[orientation][x][y] = action_name[i]

    x = init[0]
    y = init[1]
    orientation=init[2]

    policy2D[x][y] = policy[orientation][x][y]
    while policy[orientation][x][y] != '*':
        if policy[orientation][x][y]=='#':
            o2 = orientation
        elif policy[orientation][x][y]=='R':
            o2 = (orientation-1)%4
        elif policy[orientation][x][y]=='L':
            o2 = (orientation+1)%4
        x = x+forward[o2][0]
        y = y+forward[o2][1]
        orientation = o2

        policy2D[x][y] = policy[orientation][x][y]
    
    return policy2D


# In[2]:

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

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

cost = [2, 1, 20]

policy = optimum_policy2D(grid,init,goal,cost)


# In[3]:

for i in range(len(policy)):
    print policy[i]


# In[ ]:



