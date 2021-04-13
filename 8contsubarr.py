l=[1,2,3,-2,5]
temp=l[0]
l2=[]
s=len(l)
max=l[0]
for i in  range(1,s):
   temp=l[i]+temp
   l2.append(temp)
   if(temp>l2[i-2]):
       max=temp
print(max)
