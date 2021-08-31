def isPermofPali(string):
	true_length = string.replace(" ", "").lower()
	if (len(true_length)%2) == 0:
		return False
	sorted_true = sorted(true_length)
	odd = 0
	for i in range(len(sorted_true)):
		count=sorted_true.count(sorted_true[i])	
		if (count%2) == 0:
			continue
		else:
			odd += 1
			if odd > 1: return False
	if odd != 1:
		return False
	else:
		return True
		
str = raw_input('')
if isPermofPali(str):
	print 'Yes'
else:
	print 'No'