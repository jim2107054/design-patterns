class Color: # just an interface for colors
    def apply_color(self):
        pass

class Red(Color): # Concrete Implementation, implements the Color interface
    def apply_color(self):
        return "Red"

class Blue(Color): # Concrete Implementation, implements the Color interface
    def apply_color(self):
        return "Blue"
    
#Abstraction hierarchy
class Shape: # Abstraction
    def __init__(self, color: Color):
        self.color = color

    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return f"Circle with color {self.color.apply_color()}"

class Square(Shape):
    def draw(self):
        return f"Square with color {self.color.apply_color()}"
    
# Client code
if __name__ == "__main__":
    red_circle = Circle(Red())
    blue_square = Square(Blue())

    print(red_circle.draw())  # Output: Circle with color Red
    print(blue_square.draw()) # Output: Square with color Blue