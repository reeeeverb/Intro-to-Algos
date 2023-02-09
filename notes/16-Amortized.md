# Amortized Analysis
- if you had a monthly bill of $60 and a daily ycharge of $3 then you could say that you pay $5 a day
  - this is amortizing the monthly fee 
- you can do this when you analyze times as well, you simply average the time required to preform a series of data structure operations over all the operations preformed

#### Aggregate Analysis
- you show that for all n, a sequence of n operations takes T(n) worst case time in total
  - the amortized cost per operations is therefore T(n)/n
- given a sequence of random stack operations on a empty stack, you know that you can only pop as many values as you push so the worst case run time is O(n) which divides by n operations == O(1)

#### The Accouting Method
- assign differing charges to different operations

