"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
# 35 time p check n/m sa g
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        # If  value is less than the parent node than it will goes to left
        if self.value > value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else: # If new node  value greater than or equal to parent node than it will goes to right
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        
        if self.value == target:
            return True
        
        if self.value > target:
            if self.left is None:
                return False
            else:
                found = self.left.contains(target)

        elif self.value <= target:
            if self.right is None:
                return False
            else:
                found  = self.right.contains(target)

        return found        

                

    # Return the maximum value found in the tree
    def get_max(self):

        if self.right is None:
            return self.value
        max_val = self.right.get_max()
        return max_val
        
        # max_val = self.value
        # current_node = self
                       
        # while current_node:
        #     if current_node.right is None:
        #         return max_val
        #     if current_node.right.value > max_val:
        #         max_val = current_node.right.value
        #         current_node = current_node.right
        #     else:
        #         return max_val

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        
        fn(self.value)
        
        if self.left:
            self.left.for_each(fn)        
        
        if self.right:
            self.right.for_each(fn)       


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node): # Left-Node-Right LNR
        
        
        if self.left:
            self.left.in_order_print(self.left)
        
        print(self.value)
        
        if self.right:
            self.right.in_order_print(self.right)
        
 
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        
        queue = []
        queue.append(node)        
        
        while len(queue) > 0:
            current_node = queue.pop(0)
            print(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            
            if current_node.right:
                queue.append(current_node.right)
        
        
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        
        stack = []
        stack.append(node)
      
        while len(stack) > 0:
            
            current_node = stack.pop(len(stack)-1)
            print(current_node.value)
            
            if current_node.right:
                stack.append(current_node.right)

            if current_node.left:
                stack.append(current_node.left)
            
            

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node): #  Node-Left-Right NLR
        
        print(self.value)

        if self.left:
            self.left.pre_order_dft(self.left)
        
        if self.right:
            self.right.pre_order_dft(self.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node): # Left-Right-Node LRN
        
        if self.left:
            self.left.post_order_dft(self.left)
        
        if self.right:
            self.right.post_order_dft(self.right)

        print(self.value)

# root_node = BSTNode(8)
# root_node.insert(3)
# root_node.insert(4)
# root_node.insert(2)
# root_node.insert(10)
# root_node.insert(9)
# root_node.insert(12)

# # const print_node = (x) => { console.log(x) }
# print_node = lambda x: print(f'current_node is : {x}')
# root_node.for_each(print_node)

#root_node.bft_print(root_node)
#root_node.dft_print(root_node)
#root_node.in_order_print(root_node)
#root_node.pre_order_dft(root_node)
#root_node.post_order_dft(root_node)



