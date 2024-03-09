class Vehicle:
    def __init__(self, name, speed, price):
        self.name = name
        self.speed = speed
        self.price = price
    
    def __gt__(self, other):
        return self.speed > other.speed
    
    def __lt__(self, other):
        return self.speed < other.speed
    
    def __eq__(self, other):
        return self.speed == other.speed
    
    def __str__(self):
        return f"Name: {self.name}, Speed: {self.speed}, Price: {self.price}"
    
    
 
v1 = Vehicle("Name1", 100, 10000)
v2 = Vehicle("Name2", 110, 9000)

print(v1.__str__())
print(v2.__str__())

result = sorted([v1, v2])
print(v1 > v2)
print(result)

