class Point:
    def __init__(self, name, x, y):
        self.x, self.y = x, y
        self.name = name
    
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return (self.x, self.y)
    
    def __str__(self):
        return self.name + '(' + str(self.x) + ', ' + str(self.y) + ')'
    
    def __invert__(self):
        return Point(self.name, self.y, self.x)


class ColoredPoint(Point):
    def __init__(self, name, x, y, color=(0, 0, 0)):
        self.x, self.y = x, y
        self.name = name
        self.color = color
    
    def get_color(self):
        return self.color
    
    def __invert__(self):
        return ColoredPoint(self.name, self.y, self.x, 
                            color=(255 - self.color[0], 255 - self.color[1], 255 - self.color[2]))