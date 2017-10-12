# Calculate auto-correlation

import numpy as np

from MCMClongrun import A, b, sigma, m


sigma_mean = np.mean( sigma )
A_mean = np.zeros(m, np.float64)
b_mean = np.zeros(m, np.float64)
N = len(sigma);

CA      = np.zeros( (m, N), np.float64 )
Cb      = np.zeros( (m, N), np.float64 )
Csigma  = np.zeros( N, np.float64 )

rhoA      = np.zeros( (m, N), np.float64 )
rhob      = np.zeros( (m, N), np.float64 )
rhosigma  = np.zeros( N, np.float64 )

# Covariance C_A(t), C_b(t), C_sigma(t)=1/N *sum_{k=1}^{N-t}(X_k-X_mean)(X_{k+t}-X_mean). 
#I use N instead of N-t to avoid autocorrelation > 1 near the end.
for i in range(0, m):
	A_mean[i] = np.mean( A[i,:] )
	b_mean[i] = np.mean( b[i,:] )	
#	A_var[i]=np.var(A[i,:])
	for t in range(0, N):
		yA = A[i,:] - A_mean[i];
		yb = b[i,:] - b_mean[i];
		CA[i,t] = np.dot(yA[0:N-t],yA[t:N]) / N
		Cb[i,t] = np.dot(yb[0:N-t],yb[t:N]) / N
		rhoA[i,t] = CA[i,t] / CA[i,0]
		rhob[i,t] = Cb[i,t] / Cb[i,0]   


for t in range(0, N):
	y = sigma - sigma_mean
	Csigma[t] = np.dot(y[0:N-t],y[t:N]) / N
	rhosigma[t] = Csigma[t] / Csigma[0]
