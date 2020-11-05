from utils import *
from Uniform_cost import *
from Greedy_best_first_h1 import *
import time


#Load all puzzles
global puzzles
puzzles=input_puzzles('puzzles.txt')

#Solve all puzzles with Uniform_Cost


def callFunction(name,function):
    for i,puzzle in enumerate(puzzles):
        U_C=function(puzzles[i])
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
        Search_path=name+os.path.sep+'Search_files'+os.path.sep+str(i)+'_'+name+'_search.txt'
        Solution_path=name+os.path.sep+'Solution_files'+os.path.sep+str(i)+'_'+name+'_solution.txt'
        U_C.create_search_file(Search_path)
        U_C.create_solution_file(Solution_path,total_time)


callFunction('GBFH1', Greedy_best_first_h1)