from Informed_Search import *

class Greedy_best_first_h1(Informed_Search):

    def h (self,state):
        f1=np.arange(8)
        f2=np.append(np.arange(0,8,2),np.arange(1,8,2))
        h1=np.sum(state!=f1)
        h2=np.sum(state!=f2)
        # return the smalllest h
        return min(h1,h2)
    def next_node(self):
        h_min=10000
        id_min=None
        for i in range(len(self.open_list)):
            if  h_min> self.open_list[i].h:
                id_min=i
                h_min=self.open_list[i].h
        return id_min

    # def h (self, state):
    #     f1=np.arange(8)
    #     f2=np.append(np.arange(0,8,2),np.arange(1,8,2))
    #     h1=
    #     for i in range(state.len()):
    #         #2 goal state have two goal
    #             h1+=abs(i-state[i])
    #             h2+=abs(i*2%7-sate[i])
    #     # return the smalllest h
    #     return min(h1,h2)

    # def h (self, state):
    #      h1,h2
    #     for i in range(state.len()):
    #         #2 goal state have two goal
    #             for j in range(i+1,sate.len()):
    #                 if(state)
    #                 h1+=abs(i-state[i])
    #                 h2+=abs(i*2%7-sate[i])
    #     # return the smalllest h
    #     return min(h1,h2)
   