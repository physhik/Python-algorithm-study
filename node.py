class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None 
        # A reference to None will denote the fact that there is no next node. 

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext