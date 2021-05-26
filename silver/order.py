import numpy as np
u5 = np.zeros([32, 32], dtype = int) 

for i in range(21):
    u5[5*i%21][i]=1
for i in range(21,32):
    u5[i][i]=1
    
U5 = cirq.MatrixGate(u5)
CU5 = U5.controlled()

u8 = np.zeros([16, 16], dtype = int) 

for i in range(15):
    u8[8*i%15][i]=1
for i in range(15,16):
    u8[i][i]=1
    
U8 = cirq.MatrixGate(u8)
CU8 = U8.controlled()