'''
Given N observations X = {x_1,...,x_N} where x_i ~ N(mu, s^2) s.t. mu, s^2 unknown
mu ~ N(v,t)
1/s^2 ~ Gamma(a,b)
Calculate posteriors for mu and s^2
write a Gibbs sampler to sample the joint posterior distribution over m u and s^2
draw 300 samples with 100 burn-in and plot a scatter plot of mu vs s^2
'''




import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from matplotlib import colors as mcolors

if __name__ == '__main__':
	#import data
	df = pd.read_csv('data/data.csv', header = 0)


	#initialize posterior lists
	posterior = []
	post_mus = []
	post_vars = []

	#sample 300 times w/ burn-in of 100
	n = 300
	burn_in = 100

	#this is the sample mean
	sample_mean = df['data'].mean()

	#prior hyperparameters
	#nu = prior mean, tau = prior variance
	nu = 0.0
	tau = 1.0
	a = 0.1
	b = 0.1

	#initialize mu and variance
	mu = 0.5
	variance = 4.0

	#parameters of mu's conditional posterior
	c_post_mean = (variance*nu + n*tau*sample_mean)/(n*tau + variance)
	c_post_var = (variance*tau)/(n*tau + variance)
	c_post_std = np.sqrt(c_post_var)

	print c_post_mean, c_post_std

	#parameters of precision's conditional posterior
	c_post_a =	n/2 + a
	c_post_b = b + 0.5*((df['data']-mu)**2).sum()
	
	print c_post_a, c_post_b

	for i in range (0,300):
		#sample from the conditional posterior of mu
		mu = np.random.normal(c_post_mean, c_post_std)
		
		
		#sample from the conditional posterior of variance
		#note that b varies with mu
		c_post_b = b + 0.5*((df['data']-mu)**2).sum()
		variance = 1/(np.random.gamma(c_post_a, 1/c_post_b))

		#parameters of mu's conditional posterior vary w/ variance
		c_post_mean = (variance*nu + n*tau*sample_mean)/(n*tau + variance)
		c_post_var = (variance*tau)/(n*tau + variance)
		c_post_std = np.sqrt(c_post_var)

		
		post_mus.append(mu)
		post_vars.append(variance)
		posterior.append((mu, variance))

	
		
	v = np.mean(post_vars[burn_in:n])
	m = np.mean(post_mus[burn_in:n])
	

	#plot the mus and vars
	
	plt.hist(post_vars[burn_in:n], color = 'palevioletred', alpha = 0.5, bins = 20)
	plt.axvline(v, color = 'thistle')
	plt.xlabel('Sampled variance')
	plt.show()
	plt.close()

	plt.hist(post_mus[burn_in:n], color = 'teal', alpha = 0.5, bins= 20)
	plt.axvline(m, color = 'pink')
	plt.xlabel('Sampled mean')
	
	plt.show()
	plt.close()


































