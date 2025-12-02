class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None

    def length(self):
        return self.size
        
        
    def get_node(self, index) -> Node:
        temp = self.head
        for i in range(index):
            temp = temp.next
            
        return temp        
            
            
    # Without tail    
    """ def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        self.size = self.size += 1 """
        
        
    def insert_end(self, data):
        if self.tail is None:
            self.insert_first(data)
            self.size += 1
            return
        else:
            new_node = Node(data)
            self.tail.next = new_node 
            self.tail = new_node
            self.size += 1
            return
            
        
    def insert_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
        if self.tail is None:
            self.tail = self.head
            return
        self.size += 1
    
    
    def insertAt_index(self, data,index):
        if index == 0:
            self.insert_first(data)
            return
        
        if index == self.size:
            self.insert_end(data)
            return
        
        temp = self.head
        for i in range(index - 1):
            temp = temp.next
            
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node
        self.size += 1
            

    def delete_first(self):
        if self.head:
            node_to_delete = self.head.data
            temp = self.head.next
            self.head = temp
            self.head.next = temp.next
            self.size -= 1
            return node_to_delete
        else:
            print("No Element present here to delete")
        
        
    def delete_last(self):
        if(self.size <= 1):
            self.delete_first()
            self.size -= 1
            return 
            
        if self.tail:
            node_to_delete = self.tail
            secondLast = self.get_node(self.size - 3)
            self.tail = secondLast  
            secondLast.next = None
            self.size -= 1
            return node_to_delete.data
        else:
            print("No Element present here to delete")
            
            
    def delete_node_by_value(self, key):
        current = self.head
        #if value present in the head node
        if current and current.data == key:
            self.delete_first()
            return
        
        if current and self.tail.data == key:
            self.delete_last()
            return
        
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        
        node_to_delete = current
        
        if not current:
            print("Value not found")
            return
        
        prev.next = current.next
        
        return node_to_delete.data
        
    def print_linked_list(self):
        current = self.head
        if current:
            while current:
                print(current.data, end="")
                if current.next:
                    print(" -> ", end="")
                current = current.next
        else:
            print("There is nothing to print, kindly add some nodes in the Linked List")               
