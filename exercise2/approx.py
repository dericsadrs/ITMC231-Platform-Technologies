# Author's Name San Andres Deric 
# Course and Year, 2ND BS-IT 
# Honor Code which states the following: I have not given nor received any
# unathorized help in completing this exercise. I am also well aware of the policies
# stipulated in the AdNU student handbook.
# Filename        : approx.py
# Description     : This header file contains the definition of the function to approximate the value of PI.

def approx_pi(n):
	outcome=0
	
	for i in range (n): # loop 
		s = (-1) ** i / (2*i+1)
		outcome=outcome+s
	return (outcome)

#endif // APPROX_H
