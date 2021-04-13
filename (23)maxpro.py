l=[6,-3,-10,0,2]
pro=1
pro2,f=1,1
for i in range(len(l)):
    pro=pro*l[i]
    if l[i]==0:
        pro=pro
        continue
            
    pro=pro*l[i]
    if(pro<pro2):
        f=pro2
    else:
        f=pro
print(l,f)