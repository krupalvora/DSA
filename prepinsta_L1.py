#pos or neg no
""" x=int(input())
if x>0:print(True)
else:print(False) """
#sum of natural no
""" sum=0
for i in range(int(input())+1):
    sum+=i
print(sum) """
#greatest of 3
""" x,y,z=map(int,input().split(' '))
if z > max(x,y):print(z)
else:print(max(x,y)) """
#leap year
""" x=int(input())
if x%4==0:
    if x%100==0:
        if x%400==0:
            print('yes',x)
        else:
            print('NO')
    else:
            print('NO')    
else:
            print('NO') """
#prime no
""" x=int(input())
c=0
for i in range(2,x//2):
    if x%i==0:
        c+=1
if c==0:print('prime') 
# prime in range
s=int(input())
e=int(input())
for i in range(s,e+1):
    for j in range(2,i//2):
        if i%j ==0:
            break
    else:print('prime no is',i)"""
#Sum of digit of no
""" x=int(input())
sum=0
while(x>0):
    t=x%10
    sum=sum+int(t)
    x=x//10
print(sum) """
#reverse no
""" x=input()
l=[int(i) for i in str(x)]
l=l[::-1]
print(int("".join(map(str,l)))) """
#palnidrome
""" x=input()
l=[int(i) for i in str(x)]
l=l[::-1]
t=int("".join(map(str,l)))
if int(x)==t:print('Palnidrome') """
#Amstrong
""" import math
x=int(input())
sum,d=0,0
t2=x
while(t2>0):
    t2=t2//10
    d+=1
t2=x
while (t2>0):
    t=t2%10
    sum=sum+math.pow(t,d)
    t2=t2//10
print(sum,x)
if x==int(sum):print('Amstrong') """
#fibonacci 0 1 1 2 3 5 8
""" x=int(input())
s,n=0,1
print(s,n,end='')
for i  in range(2,x):
    t=n+s
    s=n
    n=t
    print('',t,end=' ')  """ 
#optimized
""" def fibonacciSeries(i):
    if i <= 1:
        return i
    else:
        return (fibonacciSeries(i - 1) + fibonacciSeries(i - 2))
if num <= 0:
    print("Please enter a Positive Number")
else:
    print("Fibonacci Series:", end=" ")
    for i in range(num):
        print(fibonacciSeries(i), end=" ") """
#factotial
""" def fact(n):
    if n==1 or n==0:
        return 1
    else :
        return n*fact(n-1)
n=int(input())
print(fact(n)) 
 """
#power of no
""" x,n=map(int,input().split(' '))
t=x
for i in range(n-1):
    t=t*x
print(t) """
#factor of no
""" n=int(input())
print('1',end=' ')
for i in range(2,n//2+1):
    if n%i==0:
        print(i,end=' ')
print(n) """
#strong no
""" def fact(n):
    if n==1 or n==0:
        return 1
    else :
        return n*fact(n-1)
n=int(input())
sum,n1=0,n
while(n1>0):
    t=n1%10
    sum=sum+fact(t)
    n1=n1//10
if sum==n:print('Estrong') """
#optimal
""" temp=n 
sum=0
f=[0]*10
f[0]=1
f[1]=1
for i in range(2,10): #precomputing the factorial value from 0 to 9 and store in the array.
    f[i]=f[i-1]*i
#Implementation
while(temp):
    r=temp%10 #r will have the vale u of the unit digit
    temp=temp//10
    sum+=f[r] #adding all the factorial  
if(sum==n):print(‘Yes’, n ,‘is strong number’) 
else:print(‘No’ , n, ‘is not a strong number’) """
#perfect sq
""" n=int(input())
import math
x=math.pow(n,0.5)
if x%1==0.0:print('Square') """
# perfect no
""" n=int(input())
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum==n:print('perfect no') """
#automorphic no
""" n=int(input())
import math
x=int(math.pow(n,2))
x=str(x)
n=str(n)
x1=''
for i in range(len(n)):
    x1=x1+x[ len(x)-len(n)+i ]
    print(i,x1)
print(x1)
if x1==str(n):print('Automorphic') """
#optimized
""" print(‘Enter the number:’)
n=int(input())
sq=n*n #square of the given number 
co=0 #condition variable
while(n>0): #loop until n becomes 0
    if(n%10!=sq%10):
        print(‘Not Automorphic’)
        co=1
        break                  
    n=n//10                      
    sq=sq//10 

if(co==0):
    print(‘Automorphic’) """
#hashed no
""" n=int(input())
x= sum(map(int, str(n)))
print(n,x,n%x) 
if n%x==0:print('Hashed')  """
#abundant no
""" 
n=int(input())
s=0
for i in range(1,n//2+1):
    if n%i==0:
        s+=i
if s>n:print('Abdudant') """
#friendly pair
""" x,y=map(int,input().split(' '))
s1=0
for i in range(1,x+1):
    if x%i==0:
        s1+=i
s2=0
for i in range(1,y+1):
    if y%i==0:
        s2+=i
print(s1,s2)
if s1/x == s2/y :print('friendly') """