from Informed_Search import *

class Uniform_cost(Informed_Search):
    


    def move(self):
        if len(self.open_list)<1:
            self.goal_state=True
            print('No Solution Found.')
        else:
            g_min=10000
            id_min=None
            for i in range(len(self.open_list)):
                if  g_min> self.open_list[i].g:
                    id_min=i
                    g_min=self.open_list[i].g


            self.current_state=self.open_list[id_min]
           
            self.is_goal_state()
            self.open_list.pop(id_min)

            self.close_list.append(self.current_state)
            
        
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
                    

    # def update_open_list(self):
        
    #         #Finds position of tile '0'
    #         id_0=self.current_state.state.argmin()

    #         #Going up or down
    #         tile=(id_0+4)%8
    #         new_state=swap(self.current_state.state,id_0,tile)
    #         self.add_to_open_list(Node(self.current_state,new_state,tile,1,1+self.current_state.g,0,0))
            
        
    #         #For extremities
    #         if id_0%4==0 or id_0%4==3:

    #             #Wrapping move
    #             tile=(int(id_0/4)*4)+3-id_0%4
    #             new_state=swap(self.current_state.state,id_0,tile)
    #             self.add_to_open_list(Node(self.current_state,new_state,tile,2,2+self.current_state.g,0,0))
                
    #             #Big Diagonal move
    #             tile=int(id_0-1+id_0%4*2/3)%8
    #             new_state=swap(self.current_state.state,id_0,tile)
    #             self.add_to_open_list(Node(self.current_state,new_state,tile,3,3+self.current_state.g,0,0))

    #             #Small Diagonal move
    #             tile=int((1-int(id_0/4))*4+1+id_0%4*2/3)
    #             new_state=swap(self.current_state.state,id_0,tile)
    #             self.add_to_open_list(Node(self.current_state,new_state,tile,3,3+self.current_state.g,0,0))

    #             #Left or Right move
    #             tile=int(id_0+1-id_0%4*2/3)
    #             new_state=swap(self.current_state.state,id_0,tile)
    #             self.add_to_open_list(Node(self.current_state,new_state,tile,1,1+self.current_state.g,0,0))

    #         else:
    #             #Going left
    #             tile=id_0-1
    #             new_state=swap(self.current_state.state,id_0,tile)
    #             self.add_to_open_list(Node(self.current_state,new_state,tile,1,1+self.current_state.g,0,0))

    #             #Going right
    #             tile=id_0+1
    #             new_state=swap(self.current_state.state,id_0,tile)
    #             self.add_to_open_list(Node(self.current_state,new_state,tile,1,1+self.current_state.g,0,0))


