from Informed_Search import *

class GBF_H1(Informed_Search):

    def h (self,node):
        h1=np.sum(node.state!=self.goal_state_1)
        h2=np.sum(node.state!=self.goal_state_2)
        # return the smalllest h
        return min(h1,h2)
    def cost_to_push(self,node):
        return node.h

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
   