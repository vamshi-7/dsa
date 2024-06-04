## Insert method in linkedList


class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        #return f"{self.head.value} -> {self.tail.value}"
        temp_value = self.head
        result = ''
        while temp_value:
            result += f"{temp_value.value}"
            if temp_value.next :
                result += ' -> '
            temp_value = temp_value.next
        return result

    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, value, index):
        
        new_node = Node(value)
        if index < 0 or index > self.length:
            raise IndexError("Index out of Bounds")
 
        elif self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node

        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1



ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(4)
ll.append(5)
ll.append(6)
ll.insert(3, 2)
ll.insert(0.1, 3)
print(ll)
print(ll.length)