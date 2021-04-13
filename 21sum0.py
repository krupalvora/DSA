l=[4,2,0,1,6]#[4 ,2 ,-3, 1, 6]
c,sum=0,0
for i in range(len(l)):
    if l[i]<=0:
        c=c+1
if(c==0):
    print('no')
for i in range(len(l)):
    for  j in range(i,len(l)):
        sum=sum+l[j]
        if sum==0:
            print('yes')
            break
    sum=0
