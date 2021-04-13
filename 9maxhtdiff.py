l=[1,5,8,10]
k=2
min,max=0,0
for i in range(len(l)):
    temp=l[i]-k
    if temp>0:
        l[i]=temp
    else:
        l[i]=k+l[i]
if(len(l)==1):
    print('list too short')
elif(len(l)==2):
    if(l[0]>l[1]):
        max=l[0]
        min=[1]
    else:
        max=l[1]
        min=[0]
else:
    for i in range(2,len(l)):
        if (l[i]>max):
            max=l[i]
        elif (l[i]<min):
            min=l[i]
print(l[len(l)-1]-l[0])