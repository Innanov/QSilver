import random, math

# randomly create a 2-dimensional quantum state
def random_qstate_by_value():
    first_entry = random.randrange(-100,101)
    second_entry = random.randrange(-100,101)
    length_square = first_entry**2+second_entry**2
    while length_square == 0:
        first_entry = random.randrange(-100,101)
        second_entry = random.randrange(-100,101)
    length_square = first_entry**2+second_entry**2
    first_entry = first_entry / length_square**0.5
    second_entry = second_entry / length_square**0.5
    return [first_entry,second_entry]
	
# randomly create a 2-dimensional quantum state	
def random_qstate_by_angle(precision=1):
    sample_angle = 360 * (10**precision)
    angle_degree = random.randrange(sample_angle)
    angle_radian = 2 * math.pi * angle_degree / sample_angle
    return [math.cos(angle_radian),math.sin(angle_radian)]	
	
# finding the angle of a 2-dimensional quantum state
def angle_qstate(x,y):
    angle_radian = math.acos(x) # radian of the angle with state |0>
    angle_degree = 360*angle_radian/(2*math.pi) # degree of the angle with state |0>
	# if the second amplitude is negative, 
	#     then angle is (-angle_degree)
	#     or equivalently 360 + (-angle_degree)
    if y<0: angle_degree = 360-angle_degree # degree of the angle
	# else degree of the angle is the same as degree of the angle with state |0>
    return angle_degree	
