from utils import *
from UCS import *
from GBF_H1 import *
from GBF_H2 import *
from Astar_h1 import *
from Astar_h2 import *
import time
import json

#Load all puzzles
global puzzles
puzzles,rows,cols=input_puzzles('puzzles.txt')

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


    #startSearch('UCS', UCS)
    #startSearch('GBF_H1', GBF_H1)
    #startSearch('GBF_H2', GBF_H2)
    #startSearch('AStar_H1', AStar_H1)
    #startSearch('AStar_H2',AStar_H2)

    #startSearch('UCS', UCS)
    startSearch('GBF_H1', GBF_H1)
    startSearch('GBF_H2', GBF_H2)
    startSearch('AStar_H1', AStar_H1)
    startSearch('AStar_H2',AStar_H2)
    get_stat()


def get_stat():
    '''
     This function generates statistics based on all existing search/solution files. Pretty prints it in .txt file and
     dumps data in a json
     '''

    stat_file_name='stat.txt'
    stat_json='stat.json'
    json_data=[]
    os.remove(stat_file_name) if os.path.exists(stat_file_name) else None
    os.remove(stat_json) if os.path.exists(stat_json) else None

    for name in ['UCS','GBF_H1','GBF_H2','AStar_H1','AStar_H2']:
        search_f_path = '{}/Search_files'.format(name)
        solution_f_path = '{}/Solution_files'.format(name)
        search_path_length=solution_path_length=solution_cost=no_solution_count=execution_time=file_count = 0

        #Get Search Files data
        for r,d,search_files in os.walk(search_f_path):
            file_count=len(search_files)
            for file in search_files:
                with open('{}/{}'.format(search_f_path,file), 'r') as f:
                    search_path_length += len(f.readlines())

        #Get Solution Files data
        for r, d, solution_files in os.walk(solution_f_path):
            for file in solution_files:
                with open('{}/{}'.format(solution_f_path,file), 'r') as f:
                    lines=f.readlines()
                    if lines[0]=='No solution found.':
                        no_solution_count+=1
                        continue
                    solution_path_length+=len(lines)-1
                    solution_cost+=float(lines[-1].split()[0])
                    execution_time+=float(lines[-1].split()[1])
        solved_file_count=file_count-no_solution_count

        # If there are stats to generate
        if(file_count>0):
            with open('stat.txt', 'a') as f:
                f.write(name + '\n')
                f.write('\tNumber of Solved Puzzles : ' + str(solved_file_count) + '\n')
                f.write('\tNumber of Unsolved Puzzles : ' + str(no_solution_count) + '\n')
                f.write('\tSolution\n')
                f.write('\t\tAverage Cost : ' + str(round(solution_cost/solved_file_count,3)) + '\n')
                f.write('\t\tAverage Execution Time : ' + str(round(execution_time/solved_file_count,3)) + '\n')
                f.write('\t\tAverage Solution Path Length : ' + str(round(solution_path_length / solved_file_count,3)) + '\n')
                f.write('\t\tTotal Cost : ' + str(solution_cost) + '\n')
                f.write('\t\tTotal Execution Time : ' + str(round(execution_time,3)) + '\n')
                f.write('\t\tTotal Solution Path Length : ' + str(solution_path_length) + '\n')
                f.write('\tSearch\n')
                f.write('\t\tAverage Search Path Length : ' + str(round(search_path_length / solved_file_count,3)) + '\n')
                f.write('\t\tTotal Search Path Length : ' + str(search_path_length) + '\n')

            json_data.append({
                "heur_name":name,
                "n_solved": solved_file_count,
                "n_unsolved": no_solution_count,
                "av_cost": ((solution_cost/solved_file_count)),
                "av_execution_time": (execution_time/solved_file_count),
                "av_sol_length": (solution_path_length / solved_file_count),
                "total_cost": solution_cost,
                "total_execution_time": execution_time,
                "total_sol_length": solution_path_length,
                "av_search_length": (search_path_length / solved_file_count),
                "total_search_length": search_path_length
            })
    #if there is json data, dump it
    if json_data:
        with open(stat_json, "w+") as outfile:
            json.dump(json_data, outfile)
if __name__ == "__main__":
    main()
