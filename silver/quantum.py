import random, math
from numpy import arcsin
from math import pi

# randomly create a 2-dimensional quantum state
def random_quantum_state():
	first_entry = random.randrange(101)
	first_entry = first_entry/100
	first_entry = first_entry**0.5 
	if random.randrange(2) == 0: 
		first_entry = -1 * first_entry
	second_entry = 1 - (first_entry**2)
	second_entry = second_entry**0.5
	if random.randrange(2) == 0: 
		second_entry = -1 * second_entry
	return [first_entry,second_entry]
	
# randomly create a 2-dimensional quantum state	
def random_quantum_state2():
	angle_degree = random.randrange(360)
	angle_radian = math.pi * angle_degree / 180
	return [math.cos(angle_radian),math.sin(angle_radian)]	
	
# finding the angle of a 2-dimensional quantum state
def angle_quantum_state(x,y):
	angle_radian = math.acos(x) # radian of the angle with state |0>
	angle_degree = 360*angle_radian/(2*math.pi) # degree of the angle with state |0>
	# if the second amplitude is negative, 
	#     then angle is (-angle_degree)
	#     or equivalently 360 + (-angle_degree)
	if y<0: angle_degree = 360-angle_degree # degree of the angle
	# else degree of the angle is the same as degree of the angle with state |0>
	return angle_degree	
	
def oracle1(circuit,quantum_reg,number):
    # prepare ancilla qubit
    # circuit.x(quantum_reg[2])
    # circuit.h(quantum_reg[2])
    if(number%2 == 0):
        circuit.x(quantum_reg[0])
    if(number < 2):
        circuit.x(quantum_reg[1])
    circuit.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[2])
    if(number < 2):
        circuit.x(quantum_reg[1])
    if(number%2 == 0):
        circuit.x(quantum_reg[0])
    # put ancilla qubit back into state |0>
    # circuit.h(quantum_reg[2])
    # circuit.x(quantum_reg[2])

def oracle2(circuit,quantum_reg,number):
    # prepare ancilla qubit
    circuit.x(quantum_reg[4])
    circuit.h(quantum_reg[4])

    if(number%2 == 0):
        circuit.x(quantum_reg[0])
    if(number%4 < 2):
        circuit.x(quantum_reg[1])
    if(number < 4):
        circuit.x(quantum_reg[2])
    circuit.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[3])
    circuit.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[4])
    circuit.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[3])
    if(number < 4):
        circuit.x(quantum_reg[2])
    if(number%4 < 2):
        circuit.x(quantum_reg[1])
    if(number%2 == 0):
        circuit.x(quantum_reg[0])

    # put ancilla qubit back into state |0>
    circuit.h(quantum_reg[4])
    circuit.x(quantum_reg[4])

def oracle3(circuit,quantum_reg,number):
    # prepare ancilla qubit
    circuit.x(quantum_reg[6])
    circuit.h(quantum_reg[6])

    if(number%2 == 0):
        circuit.x(quantum_reg[0])
    if(number%4 < 2):
        circuit.x(quantum_reg[1])
    if(number%8 < 4):
        circuit.x(quantum_reg[2])
    if(number < 8):
        circuit.x(quantum_reg[3])
    circuit.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[4])
    circuit.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[5])
    circuit.ccx(quantum_reg[4],quantum_reg[5],quantum_reg[6])
    circuit.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[5])
    circuit.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[4])
    if(number < 8):
        circuit.x(quantum_reg[3])
    if(number%8 < 4):
        circuit.x(quantum_reg[2])
    if(number%4 < 2):
        circuit.x(quantum_reg[1])
    if(number%2 == 0):
        circuit.x(quantum_reg[0])

    # put ancilla qubit back into state |0>
    circuit.h(quantum_reg[6])
    circuit.x(quantum_reg[6])

def giant_oracle(circuit99,quantum_reg,number):
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
    
    circuit99.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[10])
    circuit99.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[11])
    circuit99.ccx(quantum_reg[4],quantum_reg[5],quantum_reg[12])
    circuit99.ccx(quantum_reg[6],quantum_reg[7],quantum_reg[13])
    circuit99.ccx(quantum_reg[8],quantum_reg[9],quantum_reg[14])
    
    circuit99.ccx(quantum_reg[10],quantum_reg[11],quantum_reg[15])
    circuit99.ccx(quantum_reg[12],quantum_reg[13],quantum_reg[16])
    
    circuit99.ccx(quantum_reg[15],quantum_reg[16],quantum_reg[17])
    circuit99.ccx(quantum_reg[14],quantum_reg[17],quantum_reg[18])
    circuit99.ccx(quantum_reg[15],quantum_reg[16],quantum_reg[17])
    
    circuit99.ccx(quantum_reg[12],quantum_reg[13],quantum_reg[16])
    circuit99.ccx(quantum_reg[10],quantum_reg[11],quantum_reg[15])
    
    circuit99.ccx(quantum_reg[8],quantum_reg[9],quantum_reg[14])
    circuit99.ccx(quantum_reg[6],quantum_reg[7],quantum_reg[13])
    circuit99.ccx(quantum_reg[4],quantum_reg[5],quantum_reg[12])
    circuit99.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[11])
    circuit99.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[10])
    
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

def diffusion1(circuit,quantum_reg):
    #step 1
    # circuit.x(quantum_reg[2])
    # circuit.h(quantum_reg[2])
    
    #step 2
    circuit.h(quantum_reg[1])
    circuit.h(quantum_reg[0])
    circuit.x(quantum_reg[1])
    circuit.x(quantum_reg[0])

    #step 3
    circuit.ccx(quantum_reg[1],quantum_reg[0],quantum_reg[2])

    #step 4
    circuit.x(quantum_reg[2])

    #step 5
    circuit.x(quantum_reg[1])
    circuit.x(quantum_reg[0])
    circuit.h(quantum_reg[1])
    circuit.h(quantum_reg[0])

    #step 6
    # circuit.h(quantum_reg[2])
    # circuit.x(quantum_reg[2])

def diffusion2(circuit,quantum_reg):
    circuit.x(quantum_reg[4])
    circuit.h(quantum_reg[4])

    for i in range(3):
        circuit.h(quantum_reg[i])
        circuit.x(quantum_reg[i])

    circuit.ccx(quantum_reg[1],quantum_reg[0],quantum_reg[3])
    circuit.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[4])
    circuit.ccx(quantum_reg[1],quantum_reg[0],quantum_reg[3])

    circuit.x(quantum_reg[4])

    for i in range(3):
        circuit.x(quantum_reg[i])
        circuit.h(quantum_reg[i])

    circuit.h(quantum_reg[4])
    circuit.x(quantum_reg[4])
    
def diffusion3(circuit,quantum_reg):
    circuit.x(quantum_reg[6])
    circuit.h(quantum_reg[6])

    for i in range(4):
        circuit.h(quantum_reg[i])
        circuit.x(quantum_reg[i])

    circuit.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[4])
    circuit.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[5])
    circuit.ccx(quantum_reg[4],quantum_reg[5],quantum_reg[6])
    circuit.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[5])
    circuit.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[4])

    circuit.x(quantum_reg[6])

    for i in range(4):
        circuit.x(quantum_reg[i])
        circuit.h(quantum_reg[i])

    circuit.h(quantum_reg[6])
    circuit.x(quantum_reg[6])
    
def giant_diffusion(circuit99,quantum_reg):
    for i in range(10):
        circuit99.h(quantum_reg[i])
        circuit99.x(quantum_reg[i])

    circuit99.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[10])
    circuit99.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[11])
    circuit99.ccx(quantum_reg[4],quantum_reg[5],quantum_reg[12])
    circuit99.ccx(quantum_reg[6],quantum_reg[7],quantum_reg[13])
    circuit99.ccx(quantum_reg[8],quantum_reg[9],quantum_reg[14])
    
    circuit99.ccx(quantum_reg[10],quantum_reg[11],quantum_reg[15])
    circuit99.ccx(quantum_reg[12],quantum_reg[13],quantum_reg[16])
    
    circuit99.ccx(quantum_reg[15],quantum_reg[16],quantum_reg[17])
    circuit99.ccx(quantum_reg[14],quantum_reg[17],quantum_reg[18])
    circuit99.ccx(quantum_reg[15],quantum_reg[16],quantum_reg[17])
    
    circuit99.ccx(quantum_reg[12],quantum_reg[13],quantum_reg[16])
    circuit99.ccx(quantum_reg[10],quantum_reg[11],quantum_reg[15])
    
    circuit99.ccx(quantum_reg[8],quantum_reg[9],quantum_reg[14])
    circuit99.ccx(quantum_reg[6],quantum_reg[7],quantum_reg[13])
    circuit99.ccx(quantum_reg[4],quantum_reg[5],quantum_reg[12])
    circuit99.ccx(quantum_reg[2],quantum_reg[3],quantum_reg[11])
    circuit99.ccx(quantum_reg[0],quantum_reg[1],quantum_reg[10])

    for i in range(10):
        circuit99.x(quantum_reg[i])
        circuit99.h(quantum_reg[i])
    
    circuit99.x(quantum_reg[18])
	
def state_to_angles(current_quantum_state):
	theta = 2*arcsin(abs(round(current_quantum_state[1],4)))
	if(current_quantum_state[0] == 0 or current_quantum_state[1] == 0):
		phi = 0
	else:
		a_prime = current_quantum_state[0]/abs(current_quantum_state[0])
		angle_lambda = arcsin(abs(a_prime.imag))
		if(a_prime.real < 0 and a_prime.imag >= 0):
			angle_lambda = pi - angle_lambda
		if(a_prime.real < 0 and a_prime.imag < 0):
			angle_lambda = pi + angle_lambda
		if(a_prime.real >= 0 and a_prime.imag < 0):
			angle_lambda = 2*pi - angle_lambda
		b_prime = current_quantum_state[1]/abs(current_quantum_state[1])
		angle_nju = arcsin(abs(b_prime.imag))
		if(b_prime.real < 0 and b_prime.imag >= 0):
			angle_nju = pi - angle_nju
		if(b_prime.real < 0 and b_prime.imag < 0):
			angle_nju = pi + angle_nju
		if(b_prime.real >= 0 and b_prime.imag < 0):
			angle_nju = 2*pi - angle_nju
		phi = angle_nju - angle_lambda
	return [theta, phi]