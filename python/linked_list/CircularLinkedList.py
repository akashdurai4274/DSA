class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_first(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
            new_node.next = self.head
            self.head = new_node
            self.head.prev = new_node
            self.size += 1
        else:
            self.head = new_node
            self.tail = self.head
            self.tail.next = self.head
            self.size +=1

    def insert_index(self, index, data):
        new_node = Node(data)
        if self.size < 1 or index <= 1:
            self.insert_first(data)

        if index == self.size: 
            self.insert_last(data)

        temp = self.head
        for i in range(1, index):
            temp = temp.next
        next_node = temp.next
        temp.next = new_node
        
        new_node.next = next_node
        new_node.prev = temp
        next_node.prev = new_node
        
        self.size += 1

    def delete_first(self):
        if self.size == 0:
            return "Nothing to delete add Elements first"
        
        if self.head:
            temp = self.head.next
            self.head = temp
            self.tail.next = self.head
            self.head.prev = self.tail
        return temp.data
    
    # def delete_index():

    
    def delete_last(self):
        if self.size == 0:
            return "Nothing to delete add Elements first"
        if self.tail:
            tail = self.tail
            temp = self.tail.prev
            self.tail = temp
            temp.next = self.head
            self.head = self.tail
            return tail.data


    def insert_last(self, data):
        new_node = Node(data)

        if not self.head:
            self.insert_first(data)
            
        if self.tail:
            temp = self.tail
            self.tail.next = new_node
            self.tail = new_node
            new_node.prev = temp
            self.tail.next = self.head
            self.head.prev = self.tail
            self.size += 1

    def print(self):
        if(self.size < 1):
            print("Nothing to print")
        temp = self.tail.next
        while True:
            print(temp.data, end="")
            print(" -> ", end= "")
            temp = temp.next
            if temp == self.tail.next:
                print(self.tail.next.data)
                break



            
