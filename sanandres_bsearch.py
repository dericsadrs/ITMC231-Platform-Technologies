# San Andres Deric C
# ZT11
# Binary Search 
#1. Get values for NUMBER, n, T1, ... , Tn
#and N1
#, ... , Nn

#	2. Set the value of beginning to 1 and set the value of Found to NO
#	3. Set the value of end to n
#	4. While Found 5 NO and beginning is less than or equal to end do Steps 5
#	through 10
#	5. Set the value of m to the middle value between beginning and end
#		6. If NUMBER 5 Tm, the number found at the midpoint between beginning
#		and end, then do Steps 7 and 8
#	7. Print the name of the corresponding person, Nm
#	8. Set the value of Found to YES
#	9. Else if NUMBER , Tm, then set end 5 m 2 1
#	10. Else (NUMBER . Tm) set beginning 5 m 1 1
#	11. If (Found 5 NO) then print the message ‘Sorry, this number is not in our directory’
#	12. Stop



Number = [9,8,7,5,4,3,2,1]

n = 8
begin = 0
Found = False
end = n
toFind = 8

while(Found==False and begin<=end):
    m = int(begin+end)//2
    if Number[m] == toFind:
        print(Number[m]) 
        Found = True
				
    elif Number[m]<toFind:
        end = m - 1
    elif Number[m] > m:
        begin = m + 1
        
if Found==False:
    print("Sorry this number is not in the directory")
