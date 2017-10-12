# Create fake data

import numpy as np

# Suppose t_j (j=0,...N) are distributed evenly in [0,T]
T  = 2.0
N  = 10
dt = T / N
t  = np.zeros( N, np.float64 )  # t[0],...,t[N-1]
	
for i in range(0,N):
	t[i] = 1.0 + i * dt          # Making t cluster can accelerate the convergence.
  
# Choose parameters A_1,...,A_m, b_1,...,b_m, sigma.
# Suppose the prior has the form 1_[0,a](A)1_[0,l](b)1_[0,s](sigma)
m       = 1 
A_true       = np.zeros( m, np.float64 ) # A[0],...,A[m-1] 
b_true       = np.zeros( m, np.float64 ) # b[0],...,b[m-1] 
sigma_true   = 5.0

for i in range(0,m):   # change later
	A_true[i] = 1.0
	b_true[i] = 2.0

# Calculate true data
f  = np.zeros( N, np.float64 )  # f(t_0),...,f(t_N-1)

for i in range(0,N):
	sum = 0.0 
	for j in range(0,m):
		sum += A_true[j] * np.exp( - b_true[j] * t[i] )
	f[i] = sum


# Add Gaussian noise	
Y      = np.zeros( N, np.float64 )

for i in range(0,N):
	Y[i]    = f[i] + sigma_true * np.random.normal(0.0, 1.0)
