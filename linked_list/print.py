

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    

class linkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.len = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node:
            result += str(temp_node.value)

            if temp_node.next is not None:
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
        self.len += 1
    
nll = linkedList()
nll.append(10)
nll.append(20)
nll.append(30)
print(nll)