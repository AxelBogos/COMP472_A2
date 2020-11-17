from Informed_Search import *

class AStar_H2(Informed_Search):

    def h (self,node):
        h1=np.sum(node.state!=self.goal_state_1)
        h2=np.sum(node.state!=self.goal_state_2)
        # return the smalllest h
        return min(h1,h2)
        # return the smalllest h
        return min(h1,h2)

    def cost_to_push(self,node):
        return node.f

    def add_to_open_list(self,new_node):
        '''
         Overwrites the original function to include a check in the closed-list
        '''
        if new_node.nodeStateID not in self.close_list.keys():
            index_node=[(index,node[1]) for index,node in enumerate(self.open_list) if node[1].nodeStateID == new_node.nodeStateID]
            if not index_node:
                heappush(self.open_list,(self.cost_to_push(new_node),new_node))
            else:
                index,node=index_node[0]
                if(new_node.g<node.g):
                    #Adjust h,g,f
                    self.open_list[index][1].g=new_node.g
                    self.open_list[index][1].h=self.h(self.open_list[index][1])
                    self.open_list[index][1].f = self.open_list[index][1].h + self.open_list[index][1].g
                    #New cost in priority queue
                    self.open_list[index]=(self.cost_to_push(self.open_list[index][1]),self.open_list[index][1])
                    heapify(self.open_list)
        # unique to A*
        else:
            if self.close_list[new_node.nodeStateID].f > new_node.f:
                new_node.h=self.close_list[new_node.nodeStateID].h
                new_node.g = self.close_list[new_node.nodeStateID].g
                new_node.f = self.close_list[new_node.nodeStateID].f
                self.close_list.pop(new_node.nodeStateID)
                heappush(self.open_list, (self.cost_to_push(new_node), new_node))