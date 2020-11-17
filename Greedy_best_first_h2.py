from Informed_Search import *

class GBF_H2(Informed_Search):
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


