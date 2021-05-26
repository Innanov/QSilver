import cirq
def qpe(t,control, target, circuit, CU):
    
    #Apply Hadamard to control qubits
    circuit.append(cirq.H.on_each(control))
    
    #Apply CU gates
    for i in range(t):
        #Obtain the power of CU gate 
        CUi = CU**(2**i)
        #Apply CUi gate where t-i-1 is the control
        circuit.append(CUi(control[t-i-1],*target))
        
    #Apply inverse QFT
    iqft(t,control,circuit)
