from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.circuit.library.standard_gates import XGate

qreg =  QuantumRegister(10) 
creg = ClassicalRegister(10)
circuit = QuantumCircuit(qreg,creg)
circuit.h(qreg)
C9X = XGate().control(9)
circuit.append(C9X,list(range(1,10)) + [0])

circuit.h(qreg)    
circuit.draw()
