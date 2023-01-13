## Shuffle Left Algorithm
## San Andres Deric C

## Get values for n and the n data items
## Set the value of legit to n
## Set the value of left to 1
## Set the value of right to 2
## While left is less than or equal to legit do Steps 6 through 14
## If the item at position left is not 0 then do Steps 7 and 8
## Increase left by 1
## Increase right by 1
## Else (the item at position left is 0) do Steps 10 through 14
## Reduce legit by 1
## While right is less than or equal to n do Steps 12 and 13
## Copy the item at position right into position (right 2 1)
## Increase right by 1
## Set the value of right to (left + 1)
## Stop






#Shuffle-Left Algorithm

#1. Get values for n and the list of n values A1, A2, …, An
#2. Set legit to n
#3. Set left to 1
#4. Set right to 2
#5. Repeat steps 6-14 until left > legit
#	6.	if Aleftt ≠ 0
#	7.	Increase left by 1 
#	8.	Increase right by 1
#	9.	Else
#	10.	Reduce legit by 1
#11.  Repeat 12-13 until right > n
#12.  Copy Aight into Aright-1
#13.  Increase right by 1
#14.  Set right to left + 1
#15.Stop




n = [0, 48, 32, 0, 72, 0, 46, 32, 0, 52]
print(*n)
legit = len(n)
left = 0
right = 1
totalCountSh = 0
while left < legit:
	countSh = 0
	if n[left] != 0:
		left += 1
		right += 1
	else:
		legit -= 1
		while right < len(n):
			n[right - 1] = n[right]
			right += 1
			countSh += 1
		totalCountSh += countSh
		right = left - 1
	print(*n)
	print("Current Shuffle Count: ", countSh)
print("Total Shuffle Count: ", totalCountSh)




