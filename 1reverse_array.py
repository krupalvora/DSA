list=['a',1,2,'krupal',0]
l2=[]
x1=len(list)-1
for i in range(len(list)):
    l2.append(list[x1])
    x1=x1-1   
print(l2)   
str='krupal  vinod vora'
str2=''
x=len(str)-1
for i in range(x+1):
    str2=str2+(str[x])
    x=x-1
print(str2)