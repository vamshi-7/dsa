class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList():
    def __init__(self):
         self.head = None
         self.tail = None
         self.len = 0
        
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += '->'
            temp_node = temp_node.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.len += 1
        
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.len += 1
    
    def insert(self, index, value):
        if index < 0 or index > self.len:
            raise Exception('Index out of range!')
        elif index == 0:
            self.prepend(value)
        else:
            new_node = Node(value)
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.len += 1
    
    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
        
    def search(self, value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return True
            current = current.next
            index += 1
        return False

    def popfirst(self):
        if self.len == 0:
            return None
        popped_node = self.head

        if self.len == 1:
            self.head = None
            self.tail = None
        else:

            self.head = self.head.next
            popped_node = None
        self.len -= 1
        return popped_node

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(4)
ll.append(5)
ll.append(6)
ll.insert(2, 3)
ll.insert(3, 3)
print(ll)
#print(ll.traverse())
print(ll.popfirst())
print(ll.popfirst())
print(ll)

        

