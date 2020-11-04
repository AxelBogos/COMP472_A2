from utils import *

class Node():
    def __init__(self,Parent,state,tile,cost,g,h,f):
        #The parent node
        self.Parent=Parent
        #The current state
        self.state=state
        #The tile that was moved
        self.tile=tile
        #The cost of the move
        self.cost=cost
        #The actual cost from root
        self.g=g
        #The heuristic
        self.h=h
        #f=g+h
        self.f=f
        
class Informed_Search:

    def __init__(self,initial_state):
        self.current_state=Node(None,initial_state,0,0,0,0,0)
        self.goal_state=self.is_goal_state()
        self.open_list = []
        self.close_list = [self.current_state]

    def is_goal_state(self):
        if (self.current_state.state==np.arange(8)).all():
            self.goal_state= True
        if (self.current_state.state==np.append(np.arange(0,8,2),np.arange(1,8,2))).all():
            self.goal_state= True

        return False

    def add_to_open_list(self,new_state):
        "Need to be overwrite"
        print('Need to be overwite')
    def move(self):
        'Need to be overwrite'
        print('Need to be overwite')

    def update_open_list(self):
        
            #Finds position of tile '0'
            id_0=self.current_state.state.argmin()

            #Going up or down
            tile=(id_0+4)%8
            new_state=swap(self.current_state.state,id_0,tile)
            self.add_to_open_list(Node(self.current_state,new_state,tile,1,1+self.current_state.g,0,0))
            
        
            #For extremities
            if id_0%4==0 or id_0%4==3:

                #Wrapping move
                tile=(int(id_0/4)*4)+3-id_0%4
                new_state=swap(self.current_state.state,id_0,tile)
                self.add_to_open_list(Node(self.current_state,new_state,tile,2,2+self.current_state.g,0,0))
                
                #Big Diagonal move
                tile=int(id_0-1+id_0%4*2/3)%8
                new_state=swap(self.current_state.state,id_0,tile)
                self.add_to_open_list(Node(self.current_state,new_state,tile,3,3+self.current_state.g,0,0))

                #Small Diagonal move
                tile=int((1-int(id_0/4))*4+1+id_0%4*2/3)
                new_state=swap(self.current_state.state,id_0,tile)
                self.add_to_open_list(Node(self.current_state,new_state,tile,3,3+self.current_state.g,0,0))

                #Left or Right move
                tile=int(id_0+1-id_0%4*2/3)
                new_state=swap(self.current_state.state,id_0,tile)
                self.add_to_open_list(Node(self.current_state,new_state,tile,1,1+self.current_state.g,0,0))

            else:
                #Going left
                tile=id_0-1
                new_state=swap(self.current_state.state,id_0,tile)
                self.add_to_open_list(Node(self.current_state,new_state,tile,1,1+self.current_state.g,0,0))

                #Going right
                tile=id_0+1
                new_state=swap(self.current_state.state,id_0,tile)
                self.add_to_open_list(Node(self.current_state,new_state,tile,1,1+self.current_state.g,0,0))



    
        
    def print(self):
        print('Current State:',self.current_state.state)
        print('Close_list:')
        for l in self.close_list:
            print(' ',l.state)
        print('Open List:')
        for l in self.open_list:
            print(' ',l.state,' Cost: ',l.g)


      
    def create_search_file(self,path):
      
        with open(path,'+w') as f:
            if self.goal_state:
                for i in range(len(self.close_list)):
                    str_='0 0 '+str(self.close_list[i].cost)+' '+" ".join(str(a) for a in self.close_list[i].state)+'\n'
                    f.write(str_)
            else:
                f.write("No solution found.")

    def create_solution_file(self,path,time):
        
        with open(path,'+w') as f:
            if self.goal_state:
                state=self.current_state
                all_state=[]
                
                while(state.Parent is not None):
                    all_state.append(state)
                    state=state.Parent
                for i in range(len(all_state)-1,-1,-1):
                    str_=str(all_state[i].tile)+' '+str(all_state[i].cost)+" "+" ".join(str(a) for a in all_state[i].state)+'\n'
                    f.write(str_)

                f.write(str(self.current_state.g)+' '+str(time))
            else:
                f.write("No solution found.")

    



