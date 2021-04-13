l= [[1,3],[2,6],[8,10],[15,18]]#[[1,4],[4,5]]#[[1,3],[2,6],[8,10],[15,18]]
i,e,s,t1,t2=0,0,0,0,0
it=len(l)
while(i<it):
    print(i)
    e=l[i][1]
    s=l[i+1][0]
    t1=l[i][0]
    t2=l[i+1][1]
    if s<=e:
      print(l[i],l[i+1])
      l[i]= [t1,t2]
      l.remove(l[i+1])
      it=it-1
    it=it-1
    i=i+1
print(l)