l=[7,1,5,3,6,4]#[3,4,1,2,6]#[7,6,4,3]#[7,1,5,3,6,4]
hp,lp=max(l),min(l)
print(hp,lp)
hi,li=l.index(hp),l.index(lp)
print(hi,li) 
if (li==len(l)-1):
        print('dont buy')
        hp,lp=0,0
else:
    for i in range(len(l)):
        #buy at lp
        if(i>li):# for sell
            l=l[li+1:len(l)]
            hp=max(l)
            print('Buy at DAY',li,'Sell at',li+l.index(hp)+1)
            break
print(hp-lp)















""" l=arr
arr.sort()
print(arr)
n= len(arr)
hp,lp=arr[n-1],arr[0]
hi,li=l.index(hp),l.index(lp)
print(hp,lp)
print(l)
print(hi,li) """









""" #[7,1,5,3,6,4]
lp,hp ,ih,il= 0,0,0,0
if n == 1:
	hp = arr[0]
	lp = arr[0]

if arr[0] > arr[1]:
	hp = arr[0]
	lp = arr[1]
else:
	hp = arr[1]
	lp = arr[0]
for i in range(2, n):
	if arr[i] >hp:
	    hp = arr[i]
	elif arr[i] <lp:
	    lp = arr[i]
        ip=i """


