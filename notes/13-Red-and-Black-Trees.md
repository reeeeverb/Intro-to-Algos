## Red and Black Trees 

#### What is it and why use it
- when looking at binary trees, the speed of operations is purely dependent on the height of the tree 
- if a binary search tree becomes skewed with one side encompassing significantly more than half of the nodes, the performance of all operations will be negatively impacted
- a rb tree solves this by adding node colors that can be either red or black


#### 4 rules
- root node must be black 
- black nodes can not have black children 
- all paths from the root to a leaf must have the same number of black nodes
- all leaves are black 
