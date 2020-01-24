def isPerm(string1, string2):
	if len(string1) != len(string2):
			return False
	x = sorted(string1)		
	y = sorted(string2)
	return x==y
		
a = "kskd"
b = "kkds"

if isPerm(a,b):
	print "Yes"
else:
	print "No"