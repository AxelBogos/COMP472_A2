from utils import *
from Uniform_cost import *
import time

#Load all puzzles
puzzles=input_puzzles('puzzles.txt')

#Solve all puzzles with Uniform_Cost
for i,puzzle in enumerate(puzzles):
    U_C=Uniform_cost(puzzles[i])
    print('Begin to solve puzzle '+str(i))
    start=time.time()
    while(not U_C.goal_state):
        U_C.update_open_list()
        U_C.move()
        interval=time.time()-start
        
        if(interval>60):
            break
    
    total_time=round(time.time()-start,2)
    print(total_time,'s')
    if(U_C.goal_state):
        print('Solved!\n')
    else:
        print('No solution found.\n')
    Search_path="Search_files\\"+str(i)+'_ucs_search.txt'
    Solution_path='Solution_files\\'+str(i)+'_ucs_solution.txt'
    U_C.create_search_file(Search_path)
    U_C.create_solution_file(Solution_path,total_time)

  