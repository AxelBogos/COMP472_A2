from utils import *
from heapq import heappop,heappush,heapify

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
        #unique node_state ID
        self.nodeStateID=hash(str(state))

    def __lt__(self, other):
        return self
        
class Informed_Search:

    def __init__(self,initial_state,rows,cols):
        self.current_node=Node(None,initial_state,0,0,0,0,0)
        self.rows=rows
        self.cols=cols
        self.open_list = []
        self.close_list = {self.current_node.nodeStateID:self.current_node}
        self.goal_state_1=np.arange(self.rows*self.cols)
        self.goal_state_2=[]
        [self.goal_state_2.append(j+self.rows*i)   for j in range(self.rows) for i in range(self.cols)]
        self.goal_state=self.is_goal_state()

    def is_goal_state(self):
        if np.all(self.current_node.state==self.goal_state_1):
            self.goal_state= True
        if np.all(self.current_node.state==self.goal_state_2):
            self.goal_state= True
        return False

    def cost_to_push(self,node):
        '''Needs to be overwite
        This function should return the value to push in the priority queue
        '''

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

    def move(self):
            if not self.open_list:
                self.goal_state=True
                print('No Solution Found.')
            else:
                self.current_node=heappop(self.open_list)[1]
                self.is_goal_state()
                self.close_list[self.current_node.nodeStateID]=self.current_node

    def add_to_open_list(self,new_node):
        if new_node.nodeStateID not in self.close_list.keys():
            index_node=[(index,node[1]) for index,node in enumerate(self.open_list) if node[1].nodeStateID == new_node.nodeStateID]
            if not index_node:
                heappush(self.open_list,(self.cost_to_push(new_node),new_node))
            else:
                index,node=index_node[0]
                if(new_node.g<node.g):
                    #Adjust h,g,f
                    self.open_list[index][1].g=new_node.g
                    self.open_list[index][1].h=self.h(self.open_list[index][1])
                    self.open_list[index][1].f = self.open_list[index][1].h + self.open_list[index][1].g
                    #New cost in priority queue
                    self.open_list[index]=(self.cost_to_push(self.open_list[index][1]),self.open_list[index][1])
                    heapify(self.open_list)

    def update_open_list(self):
        
            #Finds position of tile '0'
            id_0=self.current_node.state.argmin()

            #Going up
            if(id_0>self.cols):
                tile_id=id_0-self.cols
                tile_nb=self.current_node.state[tile_id]
                new_state=swap(self.current_node.state,id_0,tile_id)
                temp=Node(self.current_node,new_state,tile_nb,1,1+self.current_node.g ,-1,-1)
                temp.h=self.h(temp)
                temp.f=self.f(temp.h,temp.g)
                self.add_to_open_list(temp)

            #Going Down
            if(id_0<self.cols*self.rows-self.cols):
                tile_id=id_0+self.cols
                tile_nb=self.current_node.state[tile_id]
                new_state=swap(self.current_node.state,id_0,tile_id)
                temp=Node(self.current_node,new_state,tile_nb,1,1+self.current_node.g ,-1,-1)
                temp.h=self.h(temp)
                temp.f=self.f(temp.h,temp.g)
                self.add_to_open_list(temp)
            
             #Going left
            if(id_0%self.cols!=0):
                tile_id=id_0-1
                tile_nb=self.current_node.state[tile_id]
                new_state=swap(self.current_node.state,id_0,tile_id)
                temp=Node(self.current_node,new_state,tile_nb,1,1+self.current_node.g ,-1,-1)
                temp.h=self.h(temp)
                temp.f=self.f(temp.h,temp.g)
                self.add_to_open_list(temp)

            #Going right
            if(id_0%self.cols!=self.cols-1):
                tile_id=id_0+1
                tile_nb=self.current_node.state[tile_id]
                new_state=swap(self.current_node.state,id_0,tile_id)
                temp=Node(self.current_node,new_state,tile_nb,1,1+self.current_node.g ,-1,-1)
                temp.h=self.h(temp)
                temp.f=self.f(temp.h,temp.g)
                self.add_to_open_list(temp)


            #For corners
            if id_0==0 or id_0==self.rows*self.cols-1 or id_0==self.cols-1 or id_0==self.rows*self.cols-self.cols:

                #Wrapping move left_right
                if id_0%self.cols==0:
                    tile_id=id_0+self.cols-1
                else:
                    tile_id=id_0-self.cols+1
                tile_nb=self.current_node.state[tile_id]
                new_state=swap(self.current_node.state,id_0,tile_id)
                temp=Node(self.current_node,new_state,tile_nb,2,2+self.current_node.g ,-1,-1)
                temp.h=self.h(temp)
                temp.f=self.f(temp.h,temp.g)
                self.add_to_open_list(temp)

                #Wrapping move up_down
                if id_0<self.cols:
                    tile_id=id_0+self.cols*(self.rows-1)
                else:
                    tile_id=id_0-self.cols*(self.rows-1)
                tile_nb=self.current_node.state[tile_id]
                new_state=swap(self.current_node.state,id_0,tile_id)
                temp=Node(self.current_node,new_state,tile_nb,2,2+self.current_node.g ,-1,-1)
                temp.h=self.h(temp)
                temp.f=self.f(temp.h,temp.g)
                self.add_to_open_list(temp)
                
                #Big Diagonal move
                if id_0<self.cols:
                    tile_id=id_0+self.cols*(self.rows-1)
                else:
                    tile_id=id_0-self.cols*(self.rows-1)
                if id_0%self.cols==0:
                    tile_id+=self.cols-1
                else:
                    tile_id+=-self.cols+1
                
                tile_nb=self.current_node.state[tile_id]
                new_state=swap(self.current_node.state,id_0,tile_id)
                temp=Node(self.current_node,new_state,tile_nb,3,3+self.current_node.g ,-1,-1)
                temp.h=self.h(temp)
                temp.f=self.f(temp.h,temp.g)
                self.add_to_open_list(temp)

                #Small Diagonal move
                if id_0<self.cols:
                    tile_id=id_0+self.cols
                else:
                    tile_id=id_0-self.cols
                if id_0%self.cols==0:
                    tile_id+=1
                else:
                    tile_id-=1
                tile_nb=self.current_node.state[tile_id]
                new_state=swap(self.current_node.state,id_0,tile_id)
                temp=Node(self.current_node,new_state,tile_nb,3,3+self.current_node.g ,-1,-1)
                temp.h=self.h(temp)
                temp.f=self.f(temp.h,temp.g)
                self.add_to_open_list(temp)

    def print(self):
        print('Current State:',self.current_node.state)
        print('Close_list:')
        for l in self.close_list.values():
            print(' ',l.state)
        print('Open List:')
        for l in self.open_list:
            print(' ',l.state,' Cost: ',l.g)

    def create_search_file(self,path):
        with open(path,'w+') as f:
            if self.goal_state:
                for i in self.close_list.keys():
                    str_=str(self.close_list[i].f)+" "+ str(self.close_list[i].g) +' '+str(self.close_list[i].h)+' '+" ".join(str(a) for a in self.close_list[i].state)+'\n'
                    f.write(str_)
            else:
                f.write("No solution found.")

    def create_solution_file(self,path,time):
        with open(path,'w+') as f:
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

    



