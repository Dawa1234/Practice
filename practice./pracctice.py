name = ord("A")
for i in range(6 ,1,-1):
	for x in range(i-1,1,-1):
		print (chr(name),end=" ")
		name += 1
	print()