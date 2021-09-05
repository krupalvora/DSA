class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,new_data):
        new_node=node(new_data)
        new_node.next=self.head
        self.head=new_node
    def insertAfter(self,pre_node,new_data):
        if pre_node is None:
            print("prevoius must be in linkedin")
            return 
        new_node=node(new_data)
        new_node.next=pre_node.next
        pre_node.next=new_node
    def append(self,new_data):
        new_node=node(new_data)
        if self.head is None:
            self.head=new_node
            return 
        last= self.head
        while (last.next):
            last=last.next
        last.next=new_node
    def PrintList(self):
        tmp=self.head
        while(tmp):
            print(tmp.data)
            tmp=tmp.next
    def getpos(self,index):
        current=self.head
        c=0
        while(current):
            if c==index:
                return current.next
            c+=1
            current=current.next
        assert(false)
        return 0
l=LinkedList()
l.push(3)
l.push(2)
l.push(1)
l.append(5)
l.append(6)
l.insertAfter(l.getpos(2),4)
l.PrintList()

