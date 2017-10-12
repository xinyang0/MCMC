# one step MCMC using Metropolis-Hastings algorithm.

def Metro_Hastings( A_old, b_old, sigma_old):
	import numpy as np
	
	from fakedata import m
	
	from likelihood import likelihood
	
	# Initial guess of the parameters
	A_new      = np.zeros( m, np.float64 )
	b_new      = np.zeros( m, np.float64 )
	
	# Suppose the proposal distribution g(theta_new|theta_old) is gaussian N(theta_old,var_prop). 
	# Generate a new candidate theta from the gaussian distribution
	var_prop = 1.0
	sigma_new = np.random.normal(sigma_old, var_prop)  


	for i in range(0,m):  
		A_new[i] = np.random.normal(A_old[i],var_prop)
		b_new[i] = np.random.normal(b_old[i],var_prop)  

	
	# Compute the log likelihood ratio
	lik_old = likelihood( A_old, b_old, sigma_old)
	lik_new = likelihood( A_new, b_new, sigma_new)
	log_r   = lik_new - lik_old
	

	accepted = 0.0
	u = 0.0
	# Accept or reject
	if (log_r > 0):    # Accept new parameters if r > 1
		accepted = 1.0  # monitor acceptance
	else:
		u = np.random.uniform(0.0,1.0)
   		if (u <  np.exp(log_r)):        # Accept new parameters with probability r.
			accepted = 1.0  # monitor acceptance
		else:
			A_new = A_old
			b_new = b_old
			sigma_new = sigma_old
			
	return A_new, b_new, sigma_new, accepted
