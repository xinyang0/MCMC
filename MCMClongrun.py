# long run MCMC to create a collection of samples of the posterior

import numpy as np

from fakedata import m

from MH import Metro_Hastings

max_iter = 30000

# Choose initial guess 
A   = np.zeros( (m, max_iter), np.float64 )
b   = np.zeros( (m, max_iter), np.float64 )
sigma  = 4.0 * np.ones( max_iter, np.float64 )
for i in range(0,m):
  	A[i,0]  = 1.5
	b[i,0]  = 2.5
	

accept_rate  = 0.0    # monitor acceptance


# Create a long run MCMC with Metropolis-Hastings
for n in range(0,max_iter-1):
	A_update, b_update, sigma_update, accept = Metro_Hastings( A[:,n], b[:,n], sigma[n])
	A[:,n+1]   = A_update
	b[:,n+1]   = b_update
	sigma[n+1] = sigma_update
	accept_rate += accept

print('Acceptance rate:', accept_rate/max_iter)
	
	

	
