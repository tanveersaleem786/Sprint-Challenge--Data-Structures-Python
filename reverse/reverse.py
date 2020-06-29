class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    # Time complexity is O(n)
    def reverse_list(self, node, prev):
        
        if node is None: 
            return 

        # check the next node
        if node.next_node:
            # recursive call
            self.reverse_list(node.next_node, node)
        else:
            # when we reach at the last node
            self.head = node

        node.next_node = prev

    # def print_list(self): 
    #     node = self.head 
    #     while(node): 
    #         print(node.value)
    #         node = node.next_node


# Driver program 
# list = LinkedList() 
# list.add_to_head(50) 
# list.add_to_head(49) 
# list.add_to_head(48) 
# list.add_to_head(47) 
# list.add_to_head(46) 
# list.add_to_head(45) 
# list.add_to_head(44) 
# list.add_to_head(43) 

# print ("linked list")
# list.print_list() 

# list.reverse_list(list.head, None)

# print( "\nReverse linked list")

# list.print_list()