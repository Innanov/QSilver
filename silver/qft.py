def qft(n,circuit):
    #Create n qubits
    qubits=cirq.LineQubit.range(n)
    #Define shorthand notation for Hadamard and Swap gates
    H = cirq.H
    swap = cirq.SWAP

    #For each qubit
    for i in range(n):
        #Apply Hadamard to the qubit
        circuit.append(H(qubits[i]))
        #Apply CR_j gates where j is the control and i is the target
        for j in range(i+1,n):
            #Define and apply CR_j gate
            crj = cirq.CZPowGate(exponent = 2/2**j)
            print(i)
            print(j)
            circuit.append(crj(qubits[j],qubits[i]))

    #Swap gates
    if n%2==0:
        k=int(n/2)
    else:
        k=int((n-1)/2)
        
    for i in range(k):
        circuit.append(swap(qubits[i],qubits[n-i-1]))
