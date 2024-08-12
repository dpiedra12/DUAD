class Node:
    data: str
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

        
class Double_Ended_Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def push_left(self, data):
        node = Node(data)
        if self.head:
            node.next = self.head
            self.head.previous = node
        else:
                self.tail = node  
        
        self.head = node  
        self.size +=1   


    def push_right(self, data):
        node = Node(data)
        if self.tail:
            node.previous = self.tail
            self.tail.next = node
        else:
                self.head = node  

        self.tail = node
        self.size +=1        


    def pop_left(self):
        if self.head is not None:
           self.head = self.head.next 

           if self.head:
               self.head.previous = None

           else:
               self.tail = None       
           self.size -= 1    


    def pop_right(self):
        if self.tail is not None:
           
            self.tail = self.tail.previous 
            if self.tail:
                self.tail.next = None

        else:
               self.head = None     
                          
        self.size -= 1    

    def print_structure(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()


deque = Double_Ended_Queue()

deque.push_left('A')
deque.push_left('B')
deque.push_left('C')

deque.print_structure()  

deque.push_right('D')
deque.push_right('E')

deque.print_structure() 

deque.pop_left()

deque.print_structure()  

deque.pop_right()

deque.print_structure()  

deque.push_right('F')

deque.print_structure()  

