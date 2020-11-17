import matplotlib.pyplot as plt
import os
class info():
    def __init__(self,Name):
        self.name=Name
        self.average_time=0
        self.average_move=0
        self.average_cost=0
        self.average_search_step=0

path_in =os.getcwd()
stats_file='{}\stats.txt'.format(path_in)
solution_path=[]
search_path=[]
path_names=[]
with open(stats_file,'w+') as f:
    f.write('')
for subdir, dirs, files in os.walk(path_in):
    for dir in dirs:
        for subdir_, dirs_, files_ in os.walk(path_in+os.sep+dir):
            for d in dirs_:
                if d=='Solution_files':
                    path_names.append(dir)
                    solution_path.append(path_in+os.sep+dir+os.sep+d)
                if d=='Search_files':
                    search_path.append(path_in+os.sep+dir+os.sep+d)
infos=[]
for name, sol_path ,search_path in zip(path_names,solution_path,search_path):
    info_=info(name)
    sol_files=[]
    search_files=[]

    for subdir, dirs, files in os.walk(search_path):
        for filename in files:
            file_in = subdir + os.sep + filename
            if file_in.endswith(".txt"):
                search_files.append(file_in)

    for subdir, dirs, files in os.walk(sol_path):
        for filename in files:
            file_in = subdir + os.sep + filename
            if file_in.endswith(".txt"):
                sol_files.append(file_in)
    nb_files=len(sol_files)
    if nb_files==0:
        continue
    total_nb_steps=0
    for file_ in search_files:
        
        with open(file_ ,'r') as f:
            nb_steps=0
            for line in f:
                nb_steps+=1
            total_nb_steps+=nb_steps

    info_.average_search_step=total_nb_steps

    for file_ in sol_files:

        with open(file_,'r') as f:
            nb_move=0
            cost=0
            time=0
            for line in f:
                line=line.split()
                if len(line)==2:
                    time=line[1]
                    cost=line[0]
                else:
                    nb_move+=1
            info_.average_cost+=int(cost)
            info_.average_move+=nb_move
            info_.average_time+=float(time)
    info_.average_cost/=nb_files
    info_.average_move/=nb_files
    info_.average_time/=nb_files
    info_.average_search_step/=nb_files
    with open(stats_file,'a') as f:
        f.write(info_.name+'\n')
        f.write('#Solution\n')
        f.write('   Average Cost : '+str(info_.average_cost)+'\n')
        f.write('   Average nb of move : '+str(info_.average_move)+'\n')
        f.write('#Search\n')
        f.write('   Average time : '+str(round(info_.average_time,2))+'s\n')
        f.write('   Average steps : '+str(info_.average_search_step)+'\n\n')

    infos.append(info_)



  




   