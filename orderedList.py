class OrderedList:
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None
    

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count
                


    
    def remove(self, item):
        current = self.head
        previous = None 
        
        found = False
        
        while not found: 
            if current.getData() == item:
                found = True # 찾았으면 루프에서 탈출

            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
            
        else:
            previous.setNext(current.getNext()) 
            
    def append(self, items): # add와 뭐가 달라야 하는지 모르겠다. 
        pass
    
    def index(self, item): # search 메쏘드에 count만 추가해서 count 출력
        current = self.head
        found = False
        
        count = 0
        while current != None and not found: # 변수를 줬을 경우엔 바로 리턴하지 않기 때문에 not found가 필요. 
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                count += 1

        return count
            
    def pop(self): #pop은 마지막 data를 주고 그 노드를 삭제. next가 None인 것을 삭제하므로 remove와도 비슷
        
        current = self.head
        previous = None
        
        while current.getNext() != None:
            previous = current 
            current = current.getNext()
        
        pop = current.getData()
        if previous == None:
            self.head = current.getNext()
            
        else:
            previous.setNext(current.getNext()) 
            
        
        return pop
    
    
    def search(self,item): # next, data 대신 그것을 정의한 메쏘드를 사용. 
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop: # 변수를 줬을 경우엔 바로 리턴하지 않기 때문에 not found가 필요. 
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True # 찾지 못하므로 룹에서 나가서 False 출력
                else:
                    current = current.getNext()

        return found
    

    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)