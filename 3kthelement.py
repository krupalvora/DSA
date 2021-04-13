list=[11,32,44,5,9,10,1]
y=int(input('enter k th element:'))-1
x=len(list)
if y>x:
    print('invalid input')
    
smallest=list[0]
for j in list:
    for i in range(1,x):
        if (list[i]<list[i-1]):
           # print(list[i],list[i-1])
            list[i-1],list[i]=list[i],list[i-1]
print(list[y])

        
