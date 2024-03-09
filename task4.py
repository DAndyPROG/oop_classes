class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)
    
    @staticmethod
    def check_radius(radius):
        
        if radius < 0:
            return False
    
        return True
    


circle = Circle.from_diameter(10)
print(circle.area())
valid = Circle.check_radius(17)
print(valid)







