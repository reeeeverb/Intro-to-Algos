## Greedy Algos
- always makes the locally optimal choice
- obv does not always yield the optimal solution

#### Steps to proving greedy is the optimal soltuion;
- Determine the optimal substructure of the problem 
  - as we did with DP
- Develop a recursive soltution
- show that if you make the greedy choice only one subproblem remain
- Prove that it is always safe to make the greedy choice 
- Develop a recursive algo that implements the greedy strategy 
- Convert the recursive algo to an iterative algo
 
### Examples:

#### Activity Selection Problem
- you are given a list of activities to schedule out in the conference room, the goal is to schedule as many activities as possible 
- the list includes each activities start and end times
- assume the activities are sorted in increasing order of finish time
- activities are considered compatiable if 2 segments do not overlap at all

