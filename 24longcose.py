l =[2,6,1,9,4,5,3,7,8,11]
n = 6
min = 0
if n == 1:
	min = l[0]
if l[0] > l[1]:
	min = l[1]
else:
	min = l[0]
for i in range(2, n):
	
	if l[i] <min:
	    min = l[i]
for i in range(len(l)):
    if ((min) in l):
        min=min+1
    else:
        break
print(min-1)
    