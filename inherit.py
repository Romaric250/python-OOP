#inheritance in OOP

class Triangle:
    def __init__(self, points):
        self._sides = 3
        self._points = list(points)
        if len(self._points) != 3:
            raise valueError("wrong number of points")

    def sides(self):
        return 3
    def __str__(self):
        return "i am a triangle"

class Square:
    def __init__(self, points):
        self._sides = 4
        self._points = list(points)                                                                                                                                                                                                                                                                                                                                                                                                                     
        if len(self._points)!= 4:
            raise valueError("Euile wrog number of points")

    def  sides(self):
        return 4

    def __str__(self):
        return "i am a square" 


print(Triangle(3,4,5).sides(), Square(4,4,45).sides())

#writing cleaner and sweet code with inheritance

class Polygon:
    def __init__(self, sides, points):
        self._points = list(points)
        self._sides = sides

    def sides(self):
        return self._sides

class Triad(Polygon):
    def __init__(self, points):
        Polygon.__init__(self, 3, points)
    
    def __str__(self):
        return "i am a triad"
    
class Squad(Polygon):
    def __init__(self, points):
        Polygon.__init__(self, 4, points)

    def __str__(self):
        return "i am a squad"



