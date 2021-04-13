l=[4, 5, 6, 7, 8, 4, 4]
n,k=8,4# element occured more than 2 times.
for i in range(len(l)):
    c=1
    temp=l[i]
    for j in range(i+1,len(l)):
        if(temp==l[j]):
            c=c+1
    if(c>(n/k)):
        print('->',temp,c)
