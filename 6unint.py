l1=[85 ,25 ,1 ,32 ,54 ,6]
l2=[85,2]
for i in range(len(l2)):
    if (l2[i] in l1):
        pass
    else:
        l1.append(l2[i])
print(len(l1))