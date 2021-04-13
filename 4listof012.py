#seen
list=[1,2,1,1,0,2,1,2,0,0,1,0,1,0]
s=0
e=len(list)-1
m=0
while(m<e):
    if(list[m]==0):
        list[s],list[m]=list[m],list[s]
        s=s+1
        m=m+1
    elif(list[m]==1):
        m=m+1
    else:
        list[m],list[e]=list[e],list[m]
        e=e-1
print(list)

    