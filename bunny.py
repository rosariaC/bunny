def convert_to_dict(matrix):
	'''
	input: N x M matrix containing positive int
	output: dictionary (nested dictionary w/ key: row index & 
	        								 val: dict w/ key: list index & val: # of carrots)
	'''
	d = {}
	for n,l in enumerate(matrix):
		d[n] = {}
		for m,val in enumerate(l):
			d[n][m] = val
	return d

def find_center(d):
	'''
	input: dictionary depicting given N x M matrix
	output: n, m index corresponding to the center indices
	'''
	max_n = len(d)
	max_m = len(d[0])
	# if both are odd numbers, then it's clear
	if max_n % 2 != 0:
		n = max_n // 2		
		if max_m % 2 != 0:
			m = max_m // 2
			return n, m
		# if row is odd but col is even
		else:
			# consider value of 2 cells & choose m where it is bigger
			m1 = max_m // 2 - 1
			m2 = max_m // 2
			compare_val = sorted([(d[n][m1], m1), (d[n][m2], m2)], reverse=True)
			m = compare_val[0][1]
			return n, m
	# if row is even:
	else:
		# consider two possible values of n
		n1 = max_n // 2 -1
		n2 = max_n // 2
		# if col is odd:
		if max_m % 2 != 0:
			m = max_m // 2
			# compare values of two possible cells
			compare_val = sorted([(d[n1][m], n1), (d[n2][m], n2)], reverse=True)
			n = compare_val[0][1]
			return n, m
		# if both row & col are even
		else:
			m1 = max_m // 2 - 1
			m2 = max_m // 2
			# need to consider 4 values
			compare_val = sorted([(d[n1][m1], n1, m1), 
								  (d[n2][m1], n2, m1),
								  (d[n1][m2], n1, m2),
								  (d[n2][m2], n2, m2)], reverse=True)
			n, m = compare_val[0][1], compare_val[0][2]
			return n, m

def bunny_moves(d, n, m):
	'''
	input: d (dictionary of gardens & remaining carrots)
		   n (row index of bunny position)
		   m (col index of bunny position)
	output: new_n (row index of where bunny will move to)
			new_m (col index of where bunny will move to)
	'''
	# make sure that the value of n & m don't exceed index
	# if exceeds max, then it will stay put where it already ate the carrot
	n_max = min(n+1, len(d)-1)
	n_min = max(n-1, 0)
	m_max = min(m+1, len(d[0])-1)
	m_min = max(m-1, 0)
	# find max value & indices of max value
	max_val = sorted([(d[n_min][m], n_min, m),
					  (d[n_max][m], n_max, m),
					  (d[n][m_min], n, m_min),
					  (d[n][m_max], n, m_max)], reverse=True)[0]
	new_n, new_m = max_val[1], max_val[2]
	return new_n, new_m

def bunny_eats(d, n, m):
	'''
	input: d (dictionary of gardens & remaining carrots)
		   n (row index of bunny position)
		   m (col index of bunny position)
	output: carrot (# of carrots eaten)
	'''
	# find number of carrots at the position
	carrot = d[n][m]
	# set number of carrots at the position to 0 (eaten)
	d[n][m] = 0
	return carrot

def is_asleep(d, n, m):
	'''
	input: d (dictionary of gardens & remaining carrots)
		   n (row index of bunny position)
		   m (col index of bunny position)
	output: boolean (asleep if all adj values = 0)
	'''
	# make sure that the value of n & m don't exceed index
	# if exceeds max, then it will stay put where it already ate the carrot
	n_max = min(n+1, len(d)-1)
	n_min = max(n-1, 0)
	m_max = min(m+1, len(d[0])-1)
	m_min = max(m-1, 0)
	# return True if the sum of adjacent squares are 0
	return not(d[n_min][m] + d[n_max][m] + d[n][m_min] + d[n][m_max])

def eat(matrix):
	'''
	input: N x M matrix containing positive int
	output: number of carros bunny eats before falling asleep
	rules:
	1. bunny starts in the center of the garden (if multiple center, choose largest number, never tie)
	2. bunny moves to adjacent cell w/ highest carrot count
	3. if no adjacent cells w/ carrots (int > 0), falls asleep
	'''
	# initialize the number of carrots
	carrots = 0
	# convert list of lists to dictionary
	d = convert_to_dict(matrix)
	# find center position
	n,m = find_center(d)
	# eat carrots at center
	carrots += bunny_eats(d, n, m)
	# while there are carrots around, bunny moves
	while not is_asleep(d, n, m):
		# new position of bunny
		new_n, new_m = bunny_moves(d, n, m)
		# bunny eats carrot at new position
		carrots += bunny_eats(d, new_n, new_m)
		# set new position
		n, m = new_n, new_m
	return carrots

# garden1 should result in 27 carrots
garden1 = [[5,7,8,6,3],
		   [0,0,7,0,4],
		   [4,6,3,4,9],
		   [3,1,0,5,8]]

# garden2 should result in 30 carrots
garden2 = [[5,7,8,6,3,0],
		   [0,0,7,0,4,1],
		   [4,6,3,8,9,2],
		   [3,1,0,5,8,3]]
