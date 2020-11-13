from Informed_Search import *

class Uniform_cost(Informed_Search):

    def h(self,state):
        return state.g

    def next_node(self):
        g_min=10000
        id_min=None
        for i in range(len(self.open_list)):
            if  g_min> self.open_list[i].g:
                id_min=i
                g_min=self.open_list[i].g
        return id_min


   
            
        
    
                    

   