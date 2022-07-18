class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter2 = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):
        circle_circumference = Circle.__pi * self.diameter2
        return circle_circumference

    def calculate_area(self):
        circle_area = Circle.__pi * self.radius * self.radius
        return circle_area

    def calculate_area_of_sector(self, angle):
        area_of_sector = (self.radius * self.radius) * (angle / 360) * Circle.__pi
        return area_of_sector

    @staticmethod
    def calculate_area_of_sector_static(radiusParam, angle):
        return radiusParam * radiusParam * (angle / 360) * Circle.__pi


circleInstance = Circle(10)
areaOfSector = circleInstance.calculate_area_of_sector(60)

areaOfSector2 = Circle.calculate_area_of_sector_static(5, 60)

print(areaOfSector)

print(areaOfSector2)

print(areaOfSector)

print(areaOfSector2)



