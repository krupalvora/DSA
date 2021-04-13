l=[1,5,7,1]
c=0
sum=6
for i in range(len(l)):
    for j in range(i,len(l)-1):
        if l[i]+l[j+1]==sum:
            c=c+1
print(c)