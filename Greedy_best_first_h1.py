from Informed_Search import *

class GBF_H1(Informed_Search):


    def h0 (self,node):
        if node.state[-1]==0:
            return 0
        return 1
        
    def h (self,node):
        h1=np.sum(node.state!=self.goal_state_1)
        h2=np.sum(node.state!=self.goal_state_2)
        # return the smalllest h
        return min(h1,h2)

    def cost_to_push(self,node):
        return node.h

