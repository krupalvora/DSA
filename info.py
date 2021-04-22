n=int(input('Enter no '))

""" def reverse(n):
    try:
        n=str(n)
        n1="".join(reversed(n))
        print(n1)
    except:
        print('e')

n1=3
n2=5
if n1+n2==reverse(n1+n2):
    print(n1,n2)
else:

    print('no') """



def palni(num):
    return str(num)=="".join(reversed(str(num)))
def tryf (n):   
    n1 = n - 1
    n2 = n + 1 
    while True:
        if palni(n1):
            break
        n1=n1-1
    #print('---------------')
    while True: 
        if palni(n2):
            break
        n2=n2+1
    sum=n1+n2
    #print(n1,n2,sum)
    if palni(sum):
         print(sum)
    else:
        tryf(n-1)
tryf(n)
