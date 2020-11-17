# :beers: COMP 472 – Assignment 2 :tiger:

[Repo URL](https://github.com/AxelBogos/COMP472_A2) <br>
---

Axel Bogos - 40077502 <br>
Luan Meiyi - 40047658 <br>
Xavier Morin - 40077865

---

## Preliminary Information


---
## Structure
#### The class "Informed_Search" is designed to be the parent class of the three childs:
* Uniform Search
* Greedy Best First
* A*
  
#### Each child should overload those two functions:
* cost_to_push(self,state):
  Which returns the appropriate cost to push in a priority queue given a state & the class
* h(self,state):
  return the Heuristic given a state

#### utils.py
 * It contains useful functions.
## How To Run 
---
Execute the main() function of ```main.py```. The main() function will execute the following function calls, in that order: 
```python
    startSearch('UCS', UCS)
    startSearch('GBF_H1', GBF_H1)
    startSearch('GBF_H2', GBF_H2)
    startSearch('AStar_H1', AStar_H1)
    startSearch('AStar_H2',AStar_H2)
    get_stat()
```
The following are generated in the excecution directory: 
```
.
| stat.txt
| stat.json
│
└───AStar_H1
|   └───Search_files
|   |   | 0_AStar_H1_search.txt
|   |   | 1_AStar_H1_search.txt
|   |   | ...
│   └───Solution_files
|   |   | 0_AStar_H1_solution.txt
|   |   | 1_AStar_H1_solution.txt
|   |   | ...
└───AStar_H2
|   └───Search_files
|   |   | 0_AStar_H2_search.txt
|   |   | 1_AStar_H2_search.txt
|   |   | ...
│   └───Solution_files
|   |   | 0_AStar_H2_solution.txt
|   |   | 1_AStar_H2_solution.txt
|   |   | ...
└───GBF_H1
|   └───Search_files
|   |   | 0_GBF_H1_search.txt
|   |   | 1_GBF_H1_search.txt
|   |   | ...
│   └───Solution_files
|   |   | 0_GBF_H1_solution.txt
|   |   | 1_GBF_H1_solution.txt
|   |   | ...
└───GBF_H2
|   └───Search_files
|   |   | 0_GBF_H2_search.txt
|   |   | 1_GBF_H2_search.txt
|   |   | ...
│   └───Solution_files
|   |   | 0_GBF_H2_solution.txt
|   |   | 1_GBF_H2_solution.txt
|   |   | ...
└───UCS
|   └───Search_files
|   |   | 0_UCS_search.txt
|   |   | 1_UCS_search.txt
|   |   | ...
│   └───Solution_files
|   |   | 0_UCS_solution.txt
|   |   | 1_UCS_solution.txt
|   |   | ...
```
---
