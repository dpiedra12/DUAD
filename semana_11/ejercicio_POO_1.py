class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14159 * (self.radius**2)

   
circle1 = Circle(5)        
print (f'The area of the circle is {circle1.get_area()}')


