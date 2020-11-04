# :beers: COMP 472 – Assignment 2 :tiger:

[Repo URL](https://github.com/AxelBogos/COMP472_A2) <br>
---

Axel Bogos - 40077502 <br>
Luan Meiyi - 40047658 <br>
Xavier Morin - 40077865

---

## Preliminary Information



#### Libraries Used:
* matplotlib
* numpy

---
## Structure
The class "Informed_Search" is designed to be the parent class of the three childs:
  -Uniform Search
  -Greedy Best First
  -A*
  
Each child should overwrite those two functions:
-Add_to_open_list(self,new_state):
  Which add the border Nodes with their informations ( G, H, F) # Mostly H and F will change
-Move(self):
  Which choose which node to visit next. # Depends on the Heuristic

Utils.py
  It contains useful functions or utilary ones.
## How To Run 

---


---
