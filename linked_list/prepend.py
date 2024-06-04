## Prepend method.

## Time and space complexity for this code O(1)

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class linkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):

        temp_node = self.head
        result = ''
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += ' -> '
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


ll = linkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.prepend(5)
ll.append(55)
print(ll)
print(ll.length)