class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.index = 0

    def append(self, item):
        
        if self.capacity == len(self.data):
            self.data[self.index] = item
            self.index += 1
            
            if self.index == self.capacity:
                self.index = 0

        else:
            self.data.append(item)

    def get(self):
        return self.data
       
    
    
# buffer = RingBuffer(3)
# buffer.append('a')
# buffer.append(2)
# buffer.append(3)

# buffer.append(4)
# buffer.append(5)
# buffer.append(6)

# buffer.append(7)
# buffer.append(8)

# buffer.get()