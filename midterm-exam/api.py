# Author's Name San Andres Deric 
# Course and Year, 2ND BS-IT 
# Honor Code which states the following: I have not given nor received any
# unathorized help in completing this exercise. I am also well aware of the policies
# stipulated in the AdNU student handbook.
# Filename        : approx.py
# Description     : 


import re
from subprocess import check_output

inputFromTheUser = input()
SplitTheInputFromTheUser =  re.split('[\'\\\\\[]]{},:]', inputFromTheUser)
SplitTheInputFromTheUser = ' '.join(SplitTheInputFromTheUser).split()

if(SplitTheInputFromTheUser[0] == 'brand_string'):
    order = r'./brand_string'
    firstOutcome = check_output(order).strip()  
    SplitTheInputFromTheUser.remove('query')
    APIDictionary = {'result' : {SplitTheInputFromTheUser[0] : firstOutcome}}

elif (SplitTheInputFromTheUser[1] == 'vendor_id'):
    order = r'./vendor_id'
    secondOutcome = check_output(order).strip()    
    SplitTheInputFromTheUser.remove('query')
    APIDictionary = {'result' : {SplitTheInputFromTheUser[1]: secondOutcome}}

else:
    print("{'error': 'Could not understand request'}")
    exit()
    
print(APIDictionary)




