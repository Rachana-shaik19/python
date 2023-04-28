from Classes.shape import Shape


class Circle(Shape):
    def __init__(self):
        super().__init__("circle")

    @property
    def name(self):
        return self.shape_name

        def draw(self):
            print("Drawing a Circle")
