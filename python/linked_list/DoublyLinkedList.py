class Node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None

    def length(self):
        return self.size
    
    def print(self):
        if self.head:
            temp = self.head
            while temp:
                print(f'{temp.data}', end=" -> "  if temp.next else "")
                temp = temp.next
            print()
        else:
            print("Nothing to Print kindly add elements")

    def insert_last(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.size += 1
        else:   
            self.insert_first(data)
            return
        
            

    def insert_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        if self.tail is None:
            self.tail = self.head
        self.size += 1

    
    def insert_index(self, index, data):
        if index == 0:
            self.insert_first(data)
            return
        if index == self.size:
            self.insert_last(data)
            return
        
        new_node = Node(data)
        temp = self.head
        for i in range(index-1):
            temp = temp.next
            
        """ temp.next = new_node
        new_node.prev = temp
        new_node.next = temp.next
        temp.next.prev = new_node """

        new_node.next = temp.next
        if temp.next:
            temp.next.prev = new_node
        new_node.prev = temp
        temp.next = new_node

        self.size +=1 

    def delete_first(self):
        if self.size <=  1:
           print("nothing to delete")
           return
        temp = self.head
        self.head = self.head.next
        if self.head:
           self.head.prev = None
        else:
            self.tail = None
        self.size -= 1
        return temp.data

    def delete_last(self):
        if self.tail is None:
            print("Nothing to delete")
            return
        temp = self.tail
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self.size -= 1
        return temp.data

    def delete_index(self, index):
        if index < 0 or index >= self.size:
            return "Invalid index"
            
        if index == 0:
            self.delete_first()

        if index == self.size:
            self.delete_last()
            
        temp = self.head
        for i in range(index):
            temp = temp.next

        temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev
        self.size -= 1
        return temp.data