# Evaluate the likelihood function L(Y|A,b,sigma) ,Y~N(f,sigma^)
#=1/(sqrt(2pi)*sigma)^n*exp(-sum((Y[i]-A exp(-\lambdat[i])^2))/2sigma^2)
# calculate log(L) to avoid too large value caused by small sigma

def likelihood( A1, b1, sigma1):
	import numpy as np
	from fakedata import t, Y, N, m, A_true, b_true, sigma_true
	
	# Calculate the coefficient in the likelihood function (log)
	c1 = 2.0 * np.pi * sigma1 * sigma1  
	c  = - N / 2.0 * np.log(c1); 
	
	# Calculate the exponential part (log) 
	sum1 = 0.0
	for i in range(0,N):
		f1 = 0.0
		for j in range(0,m):
			f1 += A1[j] * np.exp( - b1[j] * t[i] )  # f is the true value with parameters A,b,sigma.
		sum1 += ( Y[i] - f1 ) * ( Y[i] - f1 )
	e = - sum1 / (2.0 * sigma1 * sigma1)	
	
	#Suppose the prior distribution for parameters are gaussian. The mean is the true value and the variance is 1. 
	# If we use uninformative prior g(theta)=1, convergence rate is quite slow, and the sampling parameters keep increasing or decreasing in some cases.
	# And the acceptance will be too large.
	prior_A = 0.0;
	prior_b = 0.0;
	prior_sigma = 0.0;
	prior = 0.0;
	
	for j in range(0,m):
		prior_A +=  ( A1[j] - A_true[j] ) * ( A1[j] - A_true[j] ) 
		prior_b +=  ( b1[j] - b_true[j] ) * ( b1[j] - b_true[j] ) 
	prior_sigma = ( sigma1 - sigma_true ) * ( sigma1 - sigma_true ) 
	prior = - ( prior_A + prior_b + prior_sigma ) / 2.0 - 3.0 / 2.0 * m * np.log(2.0*np.pi);
	
	log_lik = c + e + prior
	return log_lik

	

