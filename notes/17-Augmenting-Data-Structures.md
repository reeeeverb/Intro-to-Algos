# Augmenting Data Structures
- in most cases you will need to add some features to a preexisting data structure in order to optimize it for your specific implementation
  - this is the spirit of augmentation

#### Dynamic Order Statistics
- an example of a structure that is optimized for stat operations is a red and black tree where each node also contains an attribute x.size which is the number of nodes other than the sentinel rooted at x
- this structure can compute an elements position in the linear set in O(lg n) 

