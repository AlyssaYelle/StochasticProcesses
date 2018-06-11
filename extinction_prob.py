import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from matplotlib import colors as mcolors

# simulate a poisson(lambda) branching process over n generations
# return list of population size at each generation
def branching_process(lam, n):
	Z = [1]
	for i in range(1,n):
		x = 0
		if Z[i-1] > 0:
			for i in range(Z[i-1]):
				x += np.random.poisson(lam)
		Z.append(x)
	return Z


# determine whether a family dies off
# if final generation is size 0
# return True
def pop_dies_off(Z):
	final_pop = Z[len(Z)-1]
	if final_pop == 0:
		return True
	return False


# run 300 branching processes
# return proportion of extinct populations 
# to approximate extinction probability
def prob_extinction(lam):
	n = 10
	trials = 300
	results = 0
	for i in range(0,trials):
		pop_over_time = branching_process(lam,n)

		if pop_dies_off(pop_over_time):
			results += 1

	return float(results)/trials


	




if __name__ == '__main__':
	
	print prob_extinction(2)

