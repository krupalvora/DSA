""" from numpy import *
m=[[1, 2, 3, 4,100],
           [5, 6, 7, 8,200],
           [9, 10, 11, 12,300],
           [13, 14, 15,16,400]]
l=[]
m2=matrix(m) 
print(m2)
c=0
def right(s,e,c):
    print('right')
    print(m[s][e],s,e,c)
    for i in range(s,len(m[s])-c):
        l.append(m[s][i])
        print(l)
    #print(i)
    down(s,i,c)
def down(s,e,c):
    s=s+1
    end=   len(m[s])-1-c#len(m[s])-c
    print('dowm')
    print(m[s][e])
    for i in range(s,end):
        l.append(m[i][e])
        print(l)#print(m[i][e]) 
    left(i,e,c)
def left(s,e,c):
    print('left',s,e,c)
    s=e-1
    print('left',s,e,c)
    end= c+ s-e  #-1
    #print()
    for i in range(s,end,-1):#(len(m[s])-c-s,-1,-1):
        l.append(m[e][i])
        print(l)#print(m[e][i])
    up(e,i,c) 
def up(s,e,c):
    c=c+1
    print('up')
    #print(s,e)  13-9-5-1
    s=s-1
    end=e#len(m[s])-2
    print(s,end)
    for i in range(s,end,-1):
        l.append(m[i][e])
        print(l)#print(m[i][e])
    right(i,e+1,c)


right(0,0,c)

 """



""" 
from numpy import *
m=[[1, 2, 3, 4,100],
           [5, 6, 7, 8,200],
           [9, 10, 11, 12,300],
           [13, 14, 15,16,400]]
l=[]
print(matrix(m))
def forloop(start,end,inc):
    if len(l)==len(m):
        break
    else:
        for i in range(start,end,inc):
            l.append(m[][])
    
def right(s,e,c):
    forloop(start,end,inc)
    down(s,e,c)
def down(s,e,c):
    forloop(start,end,inc)
    left(s,e,c)
def left(s,e,c):
    forloop(start,end,inc)
    up(s,e,c)
def up(s,e,c):
    forloop(start,end,inc)
    right(s,e,c) """
m=[ [1, 2,   3,  4],
    [5, 6,   7,  8],
    [9, 10,  11, 12],
    [13, 14, 15, 16]]
list=[]
from numpy import *
print(matrix(m))
l,r,t,b=0,len(m[0])-1,0,len(m)-1
print(l,r,t,b)
dir=0
while(t<=b and l<=r):
    if dir==0:
        print('l to r',l,r)
        for i in range(t,r+1):
            print(m[t][i])
            list.append(m[t][i])
        t=t+1
    elif dir==1:#move top to bottom
        print('t to b',t,b)
        for i in range(t,r+1):
            print(m[i][r])
            list.append(m[i][r])
        r=r-1
    elif dir==2:
        print('r to l',r,l)
        for i in range(r,l-1,-1):
            print(m[b][i])
            list.append(m[b][i])
        b=b-1
    elif dir==3:
        print('b to t',b,t)
        for i in range(b,t-1,-1):
            print(m[i][l])
            list.append(m[i][l])
        l=l+1
    dir=(dir+1)%4
print(list)