#order of apperance is not maintained.
l=[2,3,-4,-1,6,-9]#[-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
s,i=0,0
while(i<len(l)): 
    if(l[i-1]>0 and l[i+1]>0):
        i=i+2   
    if(l[i]<0):
        print(l[i],i)
        l[i],l[s]=l[s],l[i]
        print(l)
        s=s+2
    elif(s>=len(l)):
        break  
    i=i+1
