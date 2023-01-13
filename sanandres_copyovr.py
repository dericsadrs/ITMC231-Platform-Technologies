#        San Andres Deric C
#         ZT11
#	1.Copy-Over Algorithm (Fig 3.2)
#	2.Get values for n and the list of n values A1, A2, …, An
#	3.Set left to 1
#	4.Set newposition to 1
#		5.While left <= n do 
#			6.If  Aleft is non-zero 
#			7.Copy A left into B newposition 
	#			8.Copy it into position newposition in new list
#				9.Increase left by 1
#				10.Increase newposition by 1
#				11.Else increase left by 1 
#	12.Stop



#	1.Copy-Over Algorithm (Fig 3.2)
#	2.Get values for n and the list of n values A1, A2, …, An
#	3.Set left to 1
#	4.Set newposition to 1
#		5.While left <= n do 
#			6.If  Aleft is non-zero 
#			7.Copy A left into B newposition 
	#			8.Copy it into position newposition in new list
#				9.Increase left by 1
#				10.Increase newposition by 1
#				11.Else increase left by 1 
#	12.Stop



n = [1,0,5,6,8,9,0]
a = 8
left = 0
newposition = 0
new = []

while left < a-1:
    if a[left] != 0:
        new.append(n[left])
        left +=1
       
    else:
        left += 1

print(new)
