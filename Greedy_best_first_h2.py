from Informed_Search import *


class Greedy_best_first_h2(Informed_Search):
    def h (self, node):
        
        f2=np.array([0,4,1,5,2,6,3,7])
        h1=0
        h2=0
        distance1=0
        distance2=0
        for i ,obj in enumerate( node.state):
            distance1= abs(obj-i)
            distance2= abs(f2[obj]-i)
            if distance1>=4:
                h1+=(distance1-3)
            
            else:
                h1+=distance1


            if distance2>=4:
                h2+=(distance2-3)
            
            else:
                h2+=distance2
           
        # return the smalllest h
        return min(h1,h2)
    # def next_node(self):
    #     h_min=10000
    #     id_min=None
    #     for i in range(len(self.open_list)):
    #         if  h_min> self.open_list[i].h:
    #             id_min=i
    #             h_min=self.open_list[i].h
    #     return id_min