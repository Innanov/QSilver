def giant_oracle(circuit99,quantum_reg):
    number=18
    if(number%2 == 0):
        circuit99.x(quantum_reg[0])
    if(number%4 < 2):
        circuit99.x(quantum_reg[1])
    if(number%8 < 4):
        circuit99.x(quantum_reg[2])
    if(number%16 < 8):
        circuit99.x(quantum_reg[3])
    if(number%32 < 16):
        circuit99.x(quantum_reg[4])
    if(number%64 < 32):
        circuit99.x(quantum_reg[5])
    if(number%128 < 64):
        circuit99.x(quantum_reg[6])
    if(number%256 < 128):
        circuit99.x(quantum_reg[7])
    if(number%512 < 256):
        circuit99.x(quantum_reg[8])
    if(number < 512):
        circuit99.x(quantum_reg[9])
    
    circuit99.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[18])
    circuit99.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[11])
    circuit99.ccx(quantum_reg[4],quantum_reg[5],quantum_reg[12])
    circuit99.ccx(quantum_reg[6],quantum_reg[7],quantum_reg[13])
    circuit99.ccx(quantum_reg[8],quantum_reg[9],quantum_reg[14])
    
    circuit99.ccx(quantum_reg[18],quantum_reg[11],quantum_reg[15])
    circuit99.ccx(quantum_reg[12],quantum_reg[13],quantum_reg[16])
    
    circuit99.ccx(quantum_reg[15],quantum_reg[16],quantum_reg[17])
    circuit99.ccx(quantum_reg[14],quantum_reg[17],quantum_reg[10])
    circuit99.ccx(quantum_reg[15],quantum_reg[16],quantum_reg[17])
    
    circuit99.ccx(quantum_reg[12],quantum_reg[13],quantum_reg[16])
    circuit99.ccx(quantum_reg[18],quantum_reg[11],quantum_reg[15])
    
    circuit99.ccx(quantum_reg[8],quantum_reg[9],quantum_reg[14])
    circuit99.ccx(quantum_reg[6],quantum_reg[7],quantum_reg[13])
    circuit99.ccx(quantum_reg[4],quantum_reg[5],quantum_reg[12])
    circuit99.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[11])
    circuit99.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[18])
    
    if(number%2 == 0):
        circuit99.x(quantum_reg[0])
    if(number%4 < 2):
        circuit99.x(quantum_reg[1])
    if(number%8 < 4):
        circuit99.x(quantum_reg[2])
    if(number%16 < 8):
        circuit99.x(quantum_reg[3])
    if(number%32 < 16):
        circuit99.x(quantum_reg[4])
    if(number%64 < 32):
        circuit99.x(quantum_reg[5])
    if(number%128 < 64):
        circuit99.x(quantum_reg[6])
    if(number%256 < 128):
        circuit99.x(quantum_reg[7])
    if(number%512 < 256):
        circuit99.x(quantum_reg[8])
    if(number < 512):
        circuit99.x(quantum_reg[9])

def giant_oracle2(circuit99,quantum_reg):
    numbers=[12,45]
    for number in numbers:
        if(number%2 == 0):
            circuit99.x(quantum_reg[0])
        if(number%4 < 2):
            circuit99.x(quantum_reg[1])
        if(number%8 < 4):
            circuit99.x(quantum_reg[2])
        if(number%16 < 8):
            circuit99.x(quantum_reg[3])
        if(number%32 < 16):
            circuit99.x(quantum_reg[4])
        if(number%64 < 32):
            circuit99.x(quantum_reg[5])
        if(number%128 < 64):
            circuit99.x(quantum_reg[6])
        if(number%256 < 128):
            circuit99.x(quantum_reg[7])
        if(number%512 < 256):
            circuit99.x(quantum_reg[8])
        if(number < 512):
            circuit99.x(quantum_reg[9])

        circuit99.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[18])
        circuit99.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[11])
        circuit99.ccx(quantum_reg[4],quantum_reg[5],quantum_reg[12])
        circuit99.ccx(quantum_reg[6],quantum_reg[7],quantum_reg[13])
        circuit99.ccx(quantum_reg[8],quantum_reg[9],quantum_reg[14])

        circuit99.ccx(quantum_reg[18],quantum_reg[11],quantum_reg[15])
        circuit99.ccx(quantum_reg[12],quantum_reg[13],quantum_reg[16])

        circuit99.ccx(quantum_reg[15],quantum_reg[16],quantum_reg[17])
        circuit99.ccx(quantum_reg[14],quantum_reg[17],quantum_reg[10])
        circuit99.ccx(quantum_reg[15],quantum_reg[16],quantum_reg[17])

        circuit99.ccx(quantum_reg[12],quantum_reg[13],quantum_reg[16])
        circuit99.ccx(quantum_reg[18],quantum_reg[11],quantum_reg[15])

        circuit99.ccx(quantum_reg[8],quantum_reg[9],quantum_reg[14])
        circuit99.ccx(quantum_reg[6],quantum_reg[7],quantum_reg[13])
        circuit99.ccx(quantum_reg[4],quantum_reg[5],quantum_reg[12])
        circuit99.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[11])
        circuit99.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[18])

        if(number%2 == 0):
            circuit99.x(quantum_reg[0])
        if(number%4 < 2):
            circuit99.x(quantum_reg[1])
        if(number%8 < 4):
            circuit99.x(quantum_reg[2])
        if(number%16 < 8):
            circuit99.x(quantum_reg[3])
        if(number%32 < 16):
            circuit99.x(quantum_reg[4])
        if(number%64 < 32):
            circuit99.x(quantum_reg[5])
        if(number%128 < 64):
            circuit99.x(quantum_reg[6])
        if(number%256 < 128):
            circuit99.x(quantum_reg[7])
        if(number%512 < 256):
            circuit99.x(quantum_reg[8])
        if(number < 512):
            circuit99.x(quantum_reg[9])

def giant_diffusion(circuit99,quantum_reg):
    for i in range(10):
        circuit99.h(quantum_reg[i])
        circuit99.x(quantum_reg[i])

    circuit99.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[18])
    circuit99.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[11])
    circuit99.ccx(quantum_reg[4],quantum_reg[5],quantum_reg[12])
    circuit99.ccx(quantum_reg[6],quantum_reg[7],quantum_reg[13])
    circuit99.ccx(quantum_reg[8],quantum_reg[9],quantum_reg[14])
    
    circuit99.ccx(quantum_reg[18],quantum_reg[11],quantum_reg[15])
    circuit99.ccx(quantum_reg[12],quantum_reg[13],quantum_reg[16])
    
    circuit99.ccx(quantum_reg[15],quantum_reg[16],quantum_reg[17])
    circuit99.ccx(quantum_reg[14],quantum_reg[17],quantum_reg[10])
    circuit99.ccx(quantum_reg[15],quantum_reg[16],quantum_reg[17])
    
    circuit99.ccx(quantum_reg[12],quantum_reg[13],quantum_reg[16])
    circuit99.ccx(quantum_reg[18],quantum_reg[11],quantum_reg[15])
    
    circuit99.ccx(quantum_reg[8],quantum_reg[9],quantum_reg[14])
    circuit99.ccx(quantum_reg[6],quantum_reg[7],quantum_reg[13])
    circuit99.ccx(quantum_reg[4],quantum_reg[5],quantum_reg[12])
    circuit99.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[11])
    circuit99.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[18])

    for i in range(10):
        circuit99.x(quantum_reg[i])
        circuit99.h(quantum_reg[i])
    
    circuit99.x(quantum_reg[10])


def Uf(circuit,qreg):
	circuit.ccx(qreg[0],qreg[1],qreg[2])
	
def Uf_8(circuit,quantum_reg):
	circuit.x(quantum_reg[2])
	circuit.ccx(quantum_reg[2],quantum_reg[1],quantum_reg[4])
	circuit.ccx(quantum_reg[4],quantum_reg[0],quantum_reg[3])
	circuit.ccx(quantum_reg[2],quantum_reg[1],quantum_reg[4])
	circuit.x(quantum_reg[2])
	