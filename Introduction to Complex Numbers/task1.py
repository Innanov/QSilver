from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
qreg =  QuantumRegister(10) 
creg = ClassicalRegister(10)
circuit = QuantumCircuit(qreg,creg)
circuit.h(qreg[0])
for i in range(1,10):
    circuit.cx(qreg[0],qreg[i])
circuit.draw()
