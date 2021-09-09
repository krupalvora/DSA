#HCF
""" x,y=map(int,input().split(' '))
hcf=1
for i in range(1,min(x,y)+1):
    if x%i==0 and y%i==0:
        hcf=i
print(hcf) """
#lcm
""" from math import *
x,y=map(int,input().split(' '))
print(gcd(x,y))
lrg=max(x,y)
while True:
    if lrg%x==0 and lrg%y==0:
        lcm=lrg
        break
    lrg+=1
print(lcm) """
# decimal to binary 
""" n=int(input())
limit=[]
m=1
for i in range(1,n):
    if m<n:
        limit.append(m)
        m=m*2
print(limit)
s=''
for i in range(len(limit)-1,-1,-1):
    if limit[i]<=n:
        n=n-limit[i]
        s=s+'1'
    else:s=s+'0' 
print(s) """
#optimized
""" 
def fun(n):
    if n>1:
        fun(n//2)
    print(n%2,end='')
 """
#binary to decimal
""" print(bin(int(input())).replace('0b','')) """
#long
""" binary_val = num
decimal_val = 0
base = 1
while num > 0:
    rem = num % 10
    decimal_val = decimal_val + rem * base
    num = num // 10
    base = base * 2 """
#Binary to octal
""" print(oct(int(input(),2)).replace('0o','')) """
#dewcimal to octal
""" print(oct(int(input())).replace('0o','')) """
#octal to binary
""" print(bin(int(input(),8)).replace('0b','')) """
#octal to dec
""" print(str(int(input(),8))) """
# Permutations In Which N People Can Occupy R Seats In A Classroom
""" n,r=map(int,input().split(' '))
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
print(fact(n),fact(r))
print (fact(n)/fact(n-r)) """
#short
""" import math
print(math.factorial(10)) """
#check whether alpha is char or not 
""" n=input() 
#ASCII value of the input 
x=ord(n)
if(65<=x<=90 or 97<=x<=122):
    print(‘yes’ , n , ‘is an Alphabet’)
else:
    print(‘No’ , n , ‘is not an Alphabet’) """
#no to word
""" ones_digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tens_digits = [ "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen","nineteen"]
multiple_of_ten = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
power_of_ten = ["hundred", "thousand"]
s='1121'
n=len(s)
ans=''
if n==1:
    print('single digit',ones_digits[int(s)])
elif int(s)>9 and int(s)<19:
    print('double',tens_digits[int(s[1])])
else:
    for i in range(n):
        t=s[i]
        if n==4:
            ans=ans+ones_digits[int(t)]+" "
            ans=ans+power_of_ten[1]+" "
            n=n-1
        elif n==3:
            ans=ans+ones_digits[int(t)]+" "
            ans=ans+power_of_ten[0]+" "
            n=n-1
        elif n==2:
            ans=ans+multiple_of_ten[int(t)]+" "
            n=n-1
        else:
            if s[i]=='0':
                ans=ans+""
            else:
                ans=ans+ones_digits[int(t)]
    print(ans) """
#no of timmes digit occured
""" x=input()
f=input()
d={}
for i in x:
    d[i]=x.count(i)
print(d[f]) """
# no of integers has exactly x divisor
""" Number = int(input('Enter range of number :'))
Divisor = int(input('Enter exact number of divisors :'))
count1 = 0
for i in range(1,Number+1):
    count2 = 0
    for j in range(1,i+1):
        if i % j == 0:
            count2+=1
        else:
            pass
    if count2 == Divisor:
        count1+=1
        print(i,end = " ")
print('')
print(count1)   """  
#roots
""" import math
a = int(input('Enter value of a :'))
b = int(input('Enter value of b :'))
c = int(input('Enter value of c :'))
if a == 0: 
    print("a cannot be zero") 
else:
    val = b**2 - 4 * a * c 
    root = math.sqrt(abs(val)) 
    if val > 0: 
        print("Two Real Roots") 
        print((-b + root)/(2 * a)) 
        print((-b - root)/(2 * a)) 
    elif val == 0: 
        print("One Real Root") 
        print(-b / (2*a)) 
    else: 
        print("No Real Root") 
        print(- b / (2*a) , " + i", root) 
        print(- b / (2*a) , " - i", root) """