## Dynamic Programming
- Typically optimization problems where  you make a set of choicces to arrive at an optimal solution
  - each choice generates subproblems and you try to repeat subproblems so you can resuse the solutions

#### Steps to Generating a DP Algo
1) Characterize the structure of an optimal solution
2) Recursively define the value of an optimal solution
3) Compute the value of an optimal solution(usually bottom up)
4) Construct an optimal solution from computed information

#### Example 1 : Rod Cutting
- You have a rod of length n and you can cut into any number of pieces each size has a set price, make the most money
- implementation in cut-rod.py

#### Example 2 : Matrix Chain Multiplication
- given a sequence of n matrices to be multiplied compute the product
  - matrices are not neccesarily square
- multiplication of 3 different rectangaular matrixes Axa \* Bxb \* Cxc does (A\*B\*C)+(a\*b\*c) scalar mutli.
  - so as you can see, the order does matter
