class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coordinate(self):
        return self.x, self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_coordinate(self, coordinate):
        x, y = coordinate
        self.set_x(x)
        self.set_y(y)

    def add_x(self, x):
        self.x += x

    def add_y(self, y):
        self.y += y

    def multiply(self, n):
        self.x *= n
        self.y *= n

    def negative_x(self):
        self.x = -self.x

    def negative_y(self):
        self.y = -self.y
