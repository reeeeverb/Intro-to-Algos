#!/bin/python3
import math

prices = [0,1,5,8,9,10,17,17,20,24,30]
number = int(input())
remember = [-math.inf] * (number+1)
print(remember)
def memoized(p,n,r):
    q = -math.inf
    if n == 0:
        q = 0
    if r[n] >= 0:
        print("hit")
        return r[n]
    else:
        for i in range(n):
            q = max(q,p[i] + memoized(p,n-i,r))
    r[n] = q
    return q

memoized(prices,number,remember)


