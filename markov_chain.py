import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from matplotlib import colors as mcolors


if __name__ == '__main__':
	# state 1 = no lake
	# state 0 = lake
	p_00 = 0.95
	p_01 = 0.05
	p_10 = 0.01
	p_11 = 0.99
	stochastic_mtx = [[p_00,p_01],[p_10,p_11]]


	time = 1000
	t = np.arange(0,time,1)
	y = []
	init_state = np.random.randint(0,2)
	y.append(init_state)
	for i in range(1,time):
		p = np.random.uniform(0,1)
		if y[i-1] == 0:
			if p > p_00:
				next_state = 1
			else:
				next_state = y[i-1]
		if y[i-1] == 1:
			if p > p_11:
				next_state = 0
			else:
				next_state = y[i-1]
		y.append(next_state)
	
	# Note that using plt.subplots below is equivalent to using
	# fig = plt.figure() and then ax = fig.add_subplot(111)
	fig, ax = plt.subplots()
	ax.plot(t, y)

	ax.set(xlabel='time (t)', ylabel='state',
       title='Markov Chain')
	ax.grid()

	#fig.savefig("test.png")
	plt.show()









