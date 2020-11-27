import numpy as np
import os
def generate_puzzles(nb,dim,path):
    with open(path,'w+') as f:
        arr=np.arange(dim)
        for i in range(nb):
            np.random.shuffle(arr)       
            f.write(" ".join(str(a) for a in arr)+'\n')

def input_puzzles(path):
    puzzles=[]
    with open(path,'r') as f:
        dim=f.readline()
        dim=np.asarray(dim.split(),dtype='int32')
        for line in f:
            puzzle=line.split()
            puzzle=np.asarray(puzzle,dtype='int32')
            puzzles.append(puzzle)
    return puzzles,dim[0],dim[1]

def swap(state,id_1,id_2):
    new_state=state.copy()
    new_state[id_1],new_state[id_2]=new_state[id_2], new_state[id_1]
    return new_state  
#generate_puzzles(50,16,'puzzles_4x4.txt')