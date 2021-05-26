import cirq
import numpy as np

array = np.array([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, -0.4762382+0.87931631j]])

U = cirq.MatrixGate(array)
CU = U.controlled()

def Ux(x,N):

    k=1
    while(N>2**k):
        k=k+1
        
    u = np.zeros([2**k, 2**k], dtype = int) 

    for i in range(N):
        u[x*i%N][i]=1
    for i in range(N,2**k):
        u[i][i]=1
        

    XU = cirq.MatrixGate(u).controlled()
    return XU