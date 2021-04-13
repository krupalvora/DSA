
#seen full
arr = [7,1,5,3,6,4]
n = 6

min = 0
max = 0


if n == 1:
	max = arr[0]
	min = arr[0]

if arr[0] > arr[1]:
	max = arr[0]
	min = arr[1]
else:
	max = arr[1]
	min = arr[0]
for i in range(2, n):
	if arr[i] >max:
	    max = arr[i]
	elif arr[i] <min:
	    min = arr[i]
print(min,max)
""" min=list[0]
max=list[0]
x=len(list)
if(len(list)==1):
    min,max=list[0],list[0]
elif(len(list)==2):
    if (list[0]>list[1]):
        max=list[0]
        min=list[1]
    else:
        min=list[0]
        max=list[1]
else:
    for i in range(2,x):
        if(list[i]>max):
            max=list[i]
        elif(list[i]<min):
            min=list[i]
print(min,max) """