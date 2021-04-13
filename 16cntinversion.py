l=[2,4,1,3,5]
c=0
for i in range(len(l)):
    for j in range(i,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]#swap
            c=c+1
print(l,c)