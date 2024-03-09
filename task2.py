class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def square(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def area(self):
        return self.width * self.height
  
    
rect = Rectangle(2, 4)

print(rect.square())
print(rect.perimeter())
print(rect.area())
