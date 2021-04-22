""" m=[ [1, 3, 1, 5],
    [2, 2, 4, 1],
    [5, 0, 2, 3],
    [0, 6, 1, 2]] """
m=[[10, 33, 13, 15],
                  [22, 21, 4, 1],
                  [5, 0, 2, 3],
                  [0, 6, 14, 2]]
for i in range(1,len(m)):
  for j in range (len(m[0])):
    if j==0:
      a=m[j][i-1]
      c=m[j+1][i-1]
      #print(a,c,j,i,m[j][i])
      m[j][i]=max(a,c)+m[j][i]
      print(m[j][i])
    elif j==len(m)-1:
      
      a=m[j][i-1]
      b=m[j-1][i-1]
      m[j][i]=max(a,b)+m[j][i]
    else:
     a=m[j][i-1]
     b=m[j-1][i-1]
     c=m[j+1][i-1]
     m[j][i]=max(a,b,c)+m[j][i]
     
print(max([row[len(m)-1] for row in m]))