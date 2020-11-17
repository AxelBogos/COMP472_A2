from Informed_Search import *


class GBF_H2(Informed_Search):
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
        iF2=[]
        for i in range(self.cols):
            for j in range(self.rows):
                iF2.append(i+j*self.cols)   
        self.iF2=iF2
    def h (self, node):
        # for row in range(self.row)
        
        h1=0
        h2=0
        distance1=0
        distance2=0
        for i ,obj in enumerate( node.state):
            distance1= abs(obj-i)
            distance2= abs(self.iF2[obj]-i)
            if distance1>=self.cols:
                h1+=(distance1-(self.cols-1)*(distance1/(self.cols))+distance1/(self.cols))
            
            else:
                h1+=distance1


            if distance2>=self.cols:
                h2+=(distance2-(self.cols-1)*(distance2/(self.cols))+distance2/(self.cols))
            
            else:
                h2+=distance2
           
        # return the smalllest h
        return min(h1,h2)

    def cost_to_push(self,node):
        return node.h

    def next_node(self):
        h_min=10000
        id_min=None
        for i in range(len(self.open_list)):
            if  h_min> self.open_list[i].h:
                id_min=i
                h_min=self.open_list[i].h
        return id_min
