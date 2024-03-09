class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2


circle1 = Circle(20)
area = circle1.area()

print(area)
