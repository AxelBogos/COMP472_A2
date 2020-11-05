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
        self.current_node=Node(None,initial_state,0,0,0,0,0)
        self.goal_state=self.is_goal_state()
        self.open_list = []
        self.close_list = [self.current_node]

    def is_goal_state(self):
        if (self.current_node.state==np.arange(8)).all():
            self.goal_state= True
        if (self.current_node.state==np.append(np.arange(0,8,2),np.arange(1,8,2))).all():
            self.goal_state= True

        return False
    def f(self,h,g):
        '''
        Could be overwrite, but not necessarily
        '''
        return h+g

    def h(self,state):
        '''Need to be overwite
        This function should return the heuristic
        '''
        print('Need to be overwite')
        return 0
    
    def next_node(self):
        '''
        Need to be overwrite
        This function should return the index of the next Node to visit in the open_list.
        Return an int!
        '''
        print('Need to be overwrite') 
        return 0
    
    def move(self):
            if len(self.open_list)<1:
                self.goal_state=True
                print('No Solution Found.')
            else:
                next_node_id=self.next_node()
                self.current_node=self.open_list[next_node_id]
                self.is_goal_state()
                self.open_list.pop(next_node_id)
                self.close_list.append(self.current_node)

    def add_to_open_list(self,new_state):
        index=-1
        if not any( [ all(l.state==new_state.state) for l in self.close_list]):
            for i,bool_ in enumerate( [ all(l.state==new_state.state) for l in self.open_list]):
                if bool_:
                    index=i
                    break
            if index==-1:
                self.open_list.append(new_state)     
            else:
                if(new_state.g<self.open_list[index].g):
                    self.open_list[index]=new_state


    def update_open_list(self):
        
            #Finds position of tile '0'
            id_0=self.current_node.state.argmin()

            #Going up or down
            tile_id=(id_0+4)%8
            tile_nb=self.current_node.state[tile_id]
            new_state=swap(self.current_node.state,id_0,tile_id)
            h=self.h(new_state)
            g=1+self.current_node.g
            self.add_to_open_list(Node(self.current_node,new_state,tile_nb,1,g,h,self.f(h,g)))
            
        
            #For extremities
            if id_0%4==0 or id_0%4==3:

                #Wrapping move
                tile_id=(int(id_0/4)*4)+3-id_0%4
                tile_nb=self.current_node.state[tile_id]
                new_state=swap(self.current_node.state,id_0,tile_id)
                h=self.h(new_state)
                g=2+self.current_node.g
                self.add_to_open_list(Node(self.current_node,new_state,tile_nb,2,g,h,self.f(h,g)))
                
                #Big Diagonal move
                tile_id=int(id_0-1+id_0%4*2/3)%8
                tile_nb=self.current_node.state[tile_id]
                new_state=swap(self.current_node.state,id_0,tile_id)
                h=self.h(new_state)
                g=3+self.current_node.g
                self.add_to_open_list(Node(self.current_node,new_state,tile_nb,3,g,h,self.f(h,g)))

                #Small Diagonal move
                tile_id=int((1-int(id_0/4))*4+1+id_0%4*2/3)
                tile_nb=self.current_node.state[tile_id]
                new_state=swap(self.current_node.state,id_0,tile_id)
                h=self.h(new_state)
                g=3+self.current_node.g                
                self.add_to_open_list(Node(self.current_node,new_state,tile_nb,3,g,h,self.f(h,g)))

                #Left or Right move
                tile_id=int(id_0+1-id_0%4*2/3)
                tile_nb=self.current_node.state[tile_id]
                new_state=swap(self.current_node.state,id_0,tile_id)
                h=self.h(new_state)
                g=1+self.current_node.g                
                self.add_to_open_list(Node(self.current_node,new_state,tile_nb,1,g,h,self.f(h,g)))

            else:
                #Going left
                tile_id=id_0-1
                tile_nb=self.current_node.state[tile_id]
                new_state=swap(self.current_node.state,id_0,tile_id)
                h=self.h(new_state)
                g=1+self.current_node.g                
                self.add_to_open_list(Node(self.current_node,new_state,tile_nb,1,g,h,self.f(h,g)))

                #Going right
                tile_id=id_0+1
                tile_nb=self.current_node.state[tile_id]
                new_state=swap(self.current_node.state,id_0,tile_id)
                h=self.h(new_state)
                g=1+self.current_node.g                
                self.add_to_open_list(Node(self.current_node,new_state,tile_nb,1,g,h,self.f(h,g)))



    
        
    def print(self):
        print('Current State:',self.current_node.state)
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
                    str_=str(self.close_list[i].f)+" "+ str(self.close_list[i].g) +' '+str(self.close_list[i].h)+' '+" ".join(str(a) for a in self.close_list[i].state)+'\n'
                    f.write(str_)
            else:
                f.write("No solution found.")

    def create_solution_file(self,path,time):
        
        with open(path,'+w') as f:
            if self.goal_state:
                state=self.current_node
                all_state=[]
                
                while(state.Parent is not None):
                    all_state.append(state)
                    state=state.Parent
                all_state.append(state)
                for i in range(len(all_state)-1,-1,-1):
                    str_=str(all_state[i].tile)+' '+str(all_state[i].cost)+" "+" ".join(str(a) for a in all_state[i].state)+'\n'
                    f.write(str_)

                f.write(str(self.current_node.g)+' '+str(time))
            else:
                f.write("No solution found.")

    



