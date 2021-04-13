#full seen
l=[1,4,2,3,5]
s=len(l)
x=-1
pre=0
for  i in range(s-1,0,-1):
    if(l[i]>l[i-1]):
        x=i
        break
if(x==-1):
    l.reverse()
else: 
    pre=x
    for i in range(x+1,s):
        if(l[i]>l[x-1] and l[i]< l[pre]):
            pre=i
    l[x-1],l[pre]=l[pre],l[x-1]#swap  
    l[x-1:s].reverse()
print(l)
