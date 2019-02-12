values=input().split()
fi=values[0]
si=values[1]
ti=values[2]
if fi>=si and fi>=ti:
	print(fi)
elif si>=fi and si>=ti:
	print(si)
else:
	print(ti)
	
