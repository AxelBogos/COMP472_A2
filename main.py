from utils import *
from Uniform_cost import *
from Greedy_best_first_h1 import *
from Greedy_best_first_h2 import *
from Astar_h1 import *
from Astar_h2 import *
import time

#Load all puzzles
global puzzles
puzzles,rows,cols=input_puzzles('puzzles_3x5.txt')

#Solve all puzzles with Uniform_Cost

def startSearch(name,function):
    for i,puzzle in enumerate(puzzles):
        heuristic=function(puzzles[i],rows,cols)
        print('Begin to solve puzzle '+str(i))
        start=time.time()
        while(not heuristic.goal_state and time.time()-start<180):
            heuristic.update_open_list()
            heuristic.move()
        total_time=round(time.time()-start,2)
        print(total_time,'s')
        if(heuristic.goal_state):
            print('Solved!\n')
        else:
            print('No solution found.\n')
        Search_path='{}/Search_files/{}_{}_search.txt'.format(name,i,name)
        Solution_path='{}/Solution_files/{}_{}_solution.txt'.format(name,i,name)
        heuristic.create_search_file(Search_path)
        heuristic.create_solution_file(Solution_path,total_time)

def main():
    #Make sure folders exist
    for folder in ['UCS','GBF_H1','GBF_H2','AStar_H1','AStar_H2']:
        if not os.path.exists(folder):
            os.makedirs(folder)
        if not os.path.exists('{}/Search_files'.format(folder)):
            os.makedirs('{}/Search_files'.format(folder))
        if not os.path.exists('{}/Solution_files'.format(folder)):
            os.makedirs('{}/Solution_files'.format(folder))

<<<<<<< HEAD
    # callFunction('ucs', Uniform_cost)
    callFunction('GBFH2',Greedy_best_first_h2)
    # callFunction('UC',Uniform_cost)
=======
    #startSearch('UCS', UCS)
    #startSearch('GBF_H1', GBF_H1)
    #startSearch('GBF_H2', GBF_H2)
    startSearch('AStar_H1', AStar_H1)
    #startSearch('AStar_H2',AStar_H2)
>>>>>>> 7b3cd681aa56b44e52e48d25ad2f442dc0605202

if __name__ == "__main__":
    main()
