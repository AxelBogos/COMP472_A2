from Informed_Search import *

class Greedy_best_first_h2(Informed_Search):
    def h (self, state):
        f1=np.arange(8)
        f2=np.append(np.arange(0,8,2),np.arange(1,8,2))
        h1=np.absolute(state-f1)
        h2 
        # return the smalllest h
        return min(h1,h2)