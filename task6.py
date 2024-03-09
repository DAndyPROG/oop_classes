class Counter:
    def __init__(self):
        self.count = 0
        self.method_called = 0
    
    def get_count(self):
        self.count += 1
        self.method_called += 1
        return self.count
    
    
c1 = Counter()
c2 = Counter()

result = c1.get_count() 

print(c1.method_called) 


