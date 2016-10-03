class UnorderedList:

    def __init__(self):
        self.head = None # 처음에 헤드는 None을 갖지만
        
    def isEmpty(self):
        return self.head == None
    
    def add(self,item): # add 를 통해 head에 Node를 연결한다
        temp = Node(item)
        temp.setNext(self.head) # 추가 add가 있을 경우 Node를 본체 Node의 head 에 연결
        self.head = temp # 새 헤드를 명시 
        
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count
    
    def mysearch(self, item): # 직접 제작
        
        current = self.head
        
    
        while current != None:
            if current.data == item:  
                return True # 밑에 search 메쏘드처럼 변수를 줘서 마지막에 그 변수를 리턴하는 것이 안정적
        
            current = current.next
            
        return False
                

    def search(self,item): # next, data 대신 그것을 정의한 메쏘드를 사용. 
        current = self.head
        found = False
        while current != None and not found: # 변수를 줬을 경우엔 바로 리턴하지 않기 때문에 not found가 필요. 
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found
    
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