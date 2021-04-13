list=[10,12,24,5,75,65,80]
lf=[]
l=min(list)
def sort(list):
    list1=list
    list1.sort()
    return list1[1]
def fun(list):
    global l
    print('iteration')
    if len(list)>1:
        if list.index(l)==0:
               l=sort(list)
        else:
               l=min(list)
        print(l)
        print(len(list))
        if (len(list) == 2 or len(list) ==  3):
            print('if loop exe')
            sum=max(list)-min(list)
            lf.append(sum)
            list.clear()
            
        else:
            print('else loop')
            l1=list[0:list.index(l)]
            print(l1)
            fun(l1)
            l2=list[list.index(l):]
            print(l2)
            fun(l2)
            
            print('now length is ',len(list))
        return lf
    else:
        return False
print(fun(list))
