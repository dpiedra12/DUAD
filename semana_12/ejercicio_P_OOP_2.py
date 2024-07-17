from abc import ABC, abstractmethod

class Shape(ABC):

    pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod    
    def calculate_area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius =radius
                
    def calculate_perimeter(self):
        return 2 * (3.14159 * self.radius)
              
    def calculate_area(self):
        return 3.14159 * (self.radius**2)


class Square(Shape):
     def __init__(self, side):
         self.side = side
         
     def calculate_perimeter(self):
        return 4 * self.side
        
     def calculate_area(self):
        return self.side ** 2
        

class Rectangle(Shape):
     def __init__(self, length, width): 
         self.length = length
         self.width = width
         
     def calculate_perimeter(self):
        return 2 *(self.length + self.width)
   
     def calculate_area(self):
        return self.length * self.width
        
circle1 = Circle(5)
print(f'The perimeter of the circle is: {circle1.calculate_perimeter()}')
print(f"The area of the circle is: {circle1.calculate_area()}\n")

square1 = Square(4)
print(f'The perimeter of the circle is: {square1.calculate_perimeter()}')
print(f"The area of the circle is: {square1.calculate_area()}\n")

rectangle1 = Rectangle(2,4)
print(f'The perimeter of the circle is: {rectangle1.calculate_perimeter()}')
print(f"The area of the circle is: {rectangle1.calculate_area()}")

