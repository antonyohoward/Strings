a = [13, 27, 35, 40, 49, 55, 59]
b = [17, 35, 39, 40, 55, 58, 60]
match = []
matched = 0

for i in range(0, len(a)):
	for j in range(matched,len(b)):
		if a[i] == b[j]:
			match.append(a[i])
			matched = j + 1
			break
		elif a[i] > b[j]:
			continue
		matched = j 
		break

print(a)
print(b)		
print("The matching numbers are:")
		
for letters in match:
	print(letters)
	
				