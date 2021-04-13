l=[1,3,4,2,5,2]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        print(l[i],l[j])
        if(l[i]==l[j]):
            print(l[i])
            l.remove(l[i])
print(l)
