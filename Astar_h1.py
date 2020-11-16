from Informed_Search import *

class Astar_h1(Informed_Search):

    def h (self,node):
        f1=np.arange(8)
        f2=np.append(np.arange(0,8,2),np.arange(1,8,2))
        h1=np.sum(node.state!=f1)
        h2=np.sum(node.state!=f2)
        # return the smalllest h
        return min(h1,h2)

    def cost_to_push(self,node):
        return node.h