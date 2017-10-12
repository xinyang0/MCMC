#main (plot the results)
import numpy as np
import matplotlib.pyplot as plt

import MCMClongrun
from MCMClongrun import A, b, sigma, m
import autocorr
from autocorr import A_mean, b_mean, sigma_mean, rhoA, rhob, rhosigma


for i in range(0,m):
	plt.figure()
	print('mean_A',np.mean(A[i,:]))
	
	titleString1 = 'Sampling A' + str(i) + ', mean = %(mean)7.3f' % {"mean": A_mean[i]}
	plt.subplot(2,m,1) 
	
	plt.title(titleString1) 
	plt.plot(A[i,:]) 
	
	plt.subplot(2,m,2)    
	plt.title('Autocorrelation A')  
	plt.plot(rhoA[0,:])
	
	plt.figure()
	plt.hist(A[i,:], 50, normed=1, facecolor='green')
	
	
	#print('mean_b',np.mean(b[i,:]))
	#plt.figure()
	#plt.subplot(2,m,1)   
	#titleString2 = 'Sampling b' + str(i) + ', mean = %(mean)7.3f' % {"mean": b_mean[i]} 
	#plt.title(titleString2)  
	#plt.plot(b[i,:],"o")  
	#plt.subplot(2,m,2)     
	#plt.title('Autocorrelation b')   
	#plt.plot(rhob[i,:]) 
	
	#plt.figure()
	#plt.hist(b[i,:], 50, normed=1, facecolor='green', alpha=0.75)
    
#print('mean_sigma',np.mean(sigma))
#plt.figure()
#plt.subplot(2,1,1)
#titleString3 = 'Sampling sigma' + str(i) + ', mean = %(mean)7.3f' % {"mean": sigma_mean}
#plt.title(titleString3)  
#plt.plot(sigma,"o") 
#plt.subplot(2,1,2)     
#plt.title('Autocorrelation sigma')   
#plt.plot(rhosigma) 

plt.show()
