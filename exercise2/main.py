# Author's Name, San Andres Deric 
# Course and Year, 2ND BS - IT 
# Honor Code which states the following: I have not given nor received any
# unathorized help in completing this exercise. I am also well aware of the policies
# stipulated in the AdNU student handbook.

# Filename        : main.py
# Description     : This program tests the implementation of the function 
#                   to approximate the value of PI.
#
#                   Input is read from STDIN and consists of multiple lines. 
#                   The first line contains the number of test cases, T. 
#                   This is then followed by T lines containing a positive integer n.
#
#                   Output is displayed in STDOUT. The output for each case 
#                   begin with the word CASE followed by a single space, 
#                   the case number starting from 1, a colon (:), and a single space,
#                   and finally, the approximate value of PI up to fifteen (15) decimal places.

from approx import approx_pi

testCase=0; #case
t=int(input()) # for input
    
for i in range(t): # for looping 
	testCase=testCase+1;  # for iterating through the loop
	n=int(input())        
    
	outcome=approx_pi(n) # passing the value 
    	
	r= 4 * outcome
	print("CASE",testCase,end=': ')       # print
	print("{:.15f}".format(r))
