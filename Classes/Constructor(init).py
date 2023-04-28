"""
1. def __init__(self, args ):
2.__init__ method is equivalent to constructor
3. Every time an object is created from a class , __init__ method is called
4. __init__ method allows the class to initialize the object attributes
5. it only used within classes
6. __init__ method is a magic method called Dunder methods(These are special methods whose invocation happens internally
, and they start and end with double underscores)
 eg :- __add__, __len__, __str__
7. "self" must be the first argument
"""


class Pen:
    def __init__(self, color, price, pen_type):
        self.color = color
        self.price = price
        self.pen_type = pen_type

    def details(self):
        return (self.pen_type + " is " + self.color + " ink and price is " + self.price)


Pen_1 = Pen("black", "1000", "ball pen")
print(Pen_1.details())
