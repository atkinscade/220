import math


class Sphere:
    """Sphere class, input radius to return area, volume"""
    def __init__(self, radius):
        """Initial, radius"""
        self.radius = radius

    def get_radius(self):
        """Takes radius, r, and returns it"""
        return self.radius

    def surface_area(self):
        """Takes in radius r and return the surface area of the sphere"""
        area = float(4 * math.pi * self.radius ** 2)
        return area

    def volume(self):
        """Takes in radius r and returns the volume of the sphere"""
        vol = float(4/3 * math.pi * self.radius ** 3)
        return vol

