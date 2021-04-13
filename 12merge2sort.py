l1=[1,3,5]
l2=[0,2,4]
for i in l2:
    l1.append(i)
for i in range(len(l1)):
    for j in range(len(l1)):
        if l1[i]<l1[j]:
            l1[i],l1[j]=l1[j],l1s[i]
print(l1)