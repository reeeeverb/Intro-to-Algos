import numpy as np
import math

# The most simple implementation of a matrix multiply

n = int(input())

def basic_matrix(A,B,C,n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k]*B[k][j]

def split(matrix,n):
    return matrix[:n//2,:n//2],matrix[:n//2,n//2:],matrix[n//2:,:n//2],matrix[n//2:,n//2:]
    

def recursive_multiplication(A,B,C,n):
    if n == 1:
        C[0][0] = C[0][0]+A[0][0]*B[0][0]
        return
    else:
        a,b,c,d = split(A,n)
        e,f,g,h = split(B,n)
        ae = recursive_multiplication(a,e,n//2)
        bg = recursive_multiplication(b,g,n//2)
        af = recursive_multiplication(a,f,n//2)
        bh = recursive_multiplication(b,h,n//2)
        ce = recursive_multiplication(c,e,n//2)
        dg = recursive_multiplication(d,g,n//2)
        cf = recursive_multiplication(c,f,n//2)
        dh = recursive_multiplication(d,h,n//2)
        C11 = ae + bg
        C12 = af + bh
        C21 = ce + dg
        C22 = cf + dh
        return np.vstack((np.hstack((C1,C2)),np.hstack((C21,C22))))


#basic_matrix(n)
A = np.random.rand(n,n)
B = np.random.rand(n,n)
s = (n,n)
C_recursive = np.zeros((s), dtype=int)
C_basic = np.zeros((s), dtype=int)

basic_matrix(A,B,C_basic,n)
recursive_multiplication(A,B,C_recursive,n)


