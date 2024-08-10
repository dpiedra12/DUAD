class Node:
    data: str
    

    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        

class Stack:
    head: Node

    def __init__(self):
        self.head = None
        self.size = 0

    def push (self, data):
       node = Node(data, None)
       if self.head:
           node.next = self.head
           self.head = node
       else:
           self.head = node    

       self.size +=1    

    def pop(self):
       
       if self.head is not None:
           self.head = self.head.next 
           self.size -= 1    

    def  print_structure(self):
        current_node =  self.head
        
        while (current_node is not None):
            print (current_node.data)
            current_node = current_node.next



heroes = Stack()

print("Adding heroes")
heroes.push("Superman")
heroes.push("Batman")
heroes.push("Spider-man")

heroes.print_structure()

print ("\nRemoving heroes")
heroes.pop()

heroes.print_structure()
