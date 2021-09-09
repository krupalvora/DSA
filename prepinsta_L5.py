#find length without len()
""" s='krupal'
c=0
for i in s:c+=1
print(c) """
#vowels
""" l=['a','e','i','o','u']
s='aeiou'
c=0
for s in s:
    if s in l:
        c+=1
print(c) """
#optimised
""" s='Krupal vinod vora'
s=s.lower()
dic={}
for i in "aeoiu":
    c=s.count(i)
    dic[i]=c
print(dic.values()) """
#remove vowels
""" l=['a','e','i','o','u']
s='krupalvora'
c=0
for i in s:
    if i in l:
        s=s.replace(i,'')
print(s) """ 
#string palni
""" s='kvgtvk'
if s==s[::-1]:print('palni') """
#removing character from string
""" s='a123asda54'
ans=list([i for i in s if i.isalpha() ])
ans=''.join(ans)
print(ans) """
#remove emmpty spaces
""" s='kru dfjs\n jkfs'
for i in s:
    if i==' ':
        s=s.replace(i,'')
    if  '\n' in s :
       s=s.replace('\n','')   
print(s)  """
#remove brackets
""" s="[a+b(c/d)]"
for i in s:
    if i=='[' or i==']' or i=='(' or i==')':
        s=s.replace(i,"")
print(s) """
#sum of no in string
""" s='kru2jh45jn56'
sum=0
for i in s:
    try:
        int(i)
        sum=sum+int(i)
    except:
        pass
print(sum)
 """
#capatilize first and last char of string
""" s='krupal vora'
s=s.split(' ')
s1=''
for i in s:
    t=list(i)
    t[0]=t[0].upper()
    t[-1]=t[-1].upper()
    i=''.join(t)
    s1=s1+i+' '   
print(s1) """
#freqof char
""" s='bagha'
dic={}
for i in s:
    c=s.count(i)
    dic[i]=c
print(dic.values)
print(dic['a']) """
#remove non repeating chars
""" s='fdfwkjfdsdjffh'
s=list(s)
dic={}
for i in s:
    c=s.count(i)
    dic[i]=c
print(dic)
s=''.join(s)
for i in s:
    if dic[i]>1: 
        s=s.replace(i,'')
print(s) """
#replace sub string
""" string=input(“Enter String :\n“)
str1=input(“Enter substring which has to be replaced :\n“)
str2=input(“Enter substring with which str1 has to be replaced :\n“)
string=string.replace(str1,str2)
print(“String after replacement”)
print(string) """
#count common subsequence
""" n=input()
m=input()
l1,l2=len(n),len(m)
stri=[]
cnt=[[0 for i in range(l2+1)] for i in range(l1+1)]
for i in range(1,l1+1):
    for j in range(1,l2+1):
         if(n[i-1] == m[j-1]):
             print(n[i],n[j])
             print(n[i-1],n[j-1])
             cnt[i][j] = 1 + cnt[i][j-1] + cnt[i-1][j]
             
         else:
             cnt[i][j] = cnt[i][j-1] + cnt[i-1][j] - cnt[i-1][j-1] 
print(cnt,'\n',cnt[l1])
print(stri) """
#wildcard
""" 
def solve(a,b):
    n,m=len(a),len(b)
    if n==0 and m==0:
        return True
    if n > 1 and a[0] == '*' and m == 0:
        return False
    if (n > 1 and a[0] == '?') or (n != 0 and m !=0 and a[0] == b[0]):
        return solve(a[1:],b[1:])
    if n !=0 and a[0] == '*':
        return solve(a[1:],b) or solve(a,b[1:])
    return False
str1=input('Enter string containing wild characters:\n')
str2=input('Enter string to be matched:\n')
print(solve(str1,str2))
"""
