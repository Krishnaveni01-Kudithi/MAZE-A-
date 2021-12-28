from pyamaze import maze,agent
from queue import PriorityQueue
# this is manhattan distance calculation
def h(cell1,cell2):
    x1,y1=cell1
    x2,y2=cell2
    return abs(x1-x2) + abs(y1-y2)
# here we intialize g(n) and f(n)
# g(n) for starting cell is 0 and is infinite for remaining cells
# f(n) for starting cell is only manhattan distance for starting cell as g(n) is 0 
def aStar(m):
    start=(m.rows,m.cols)
    g_score={cell:float('inf') for cell in m.grid}
    g_score[start]=0
    f_score={cell:float('inf') for cell in m.grid}
    f_score[start]=h(start,(1,1))
# intialize a priority queue named pq and put the starting cell in it with these values- f(n),h(n) and starting cell  
    pq=PriorityQueue()
    pq.put((h(start,(1,1)),h(start,(1,1)),start))
# intialize a dictionary named aPath
    aPath={}
# this loop will execute until the priority queue is empty 
    while not pq.empty():
# we get the third parameter from the tuple and name as currCell
        currCell=pq.get()[2]
# if it is equal to the goal node we break 
        if currCell==(1,1):
            break

# if it is not equal to goal node the following loop will be executed
# E for east, S for north, N for north , S for south
# we find four neighbours for each cell 
# if the value is 1 then path is available if value is 0 path is not available

        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
# if the direction is east then the nextCell will have same value of row and column value is one more than the previous one.
                if d=='E':
                    nextCell=(currCell[0],currCell[1]+1)
# if the direction is west then the nextCell will have same value of row and column value is one more than the previous one.
                if d=='W':
                    nextCell=(currCell[0],currCell[1]-1)
# if the direction is north then the nextCell will have same value of column and row value is one less than the previous one.
                if d=='N':
                    nextCell=(currCell[0]-1,currCell[1])
# if the direction is south then the nextCell will have same value of column and row value is one more than the previous one.
                if d=='S':
                    nextCell=(currCell[0]+1,currCell[1])
# the new g(n) is g(n) of current cell added to 1
                temp_g_score=g_score[currCell]+1
# the new f(n) is sum of new g(n) and manhattan distance between the new nextcell and the goal node
                temp_f_score=temp_g_score+h(nextCell,(1,1))
# if the new f(n) is less than the previous f(n) , update them and add into the priority queue
                if temp_f_score < f_score[nextCell]:
                    g_score[nextCell]= temp_g_score
                    f_score[nextCell]= temp_f_score
                    pq.put((temp_f_score,h(nextCell,(1,1)),nextCell))
# in the apath dictionary we store nextcell as the key and the currcell as the value
                    aPath[nextCell]=currCell
# we get reverse path from goal to start
# for forward path we need to invert the directions
# declare another dictionary called fwdPath
    fwdPath={}
# start from goal node 
    cell=(1,1)
# this loop is executed until we reach start node 
    while cell!=start:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]
    return fwdPath

if __name__=='__main__':
# create a maze with 5 rows and 5 columns
    m=maze(5,5)
    m.CreateMaze()
# assign the output to path
    path=aStar(m)

    a=agent(m,footprints=True)
# an agent is created 
# trace path will have agent as key  and path as value 
    m.tracePath({a:path})
    
 # an agent will follow the path 
    m.run()