# Class demo

class Vehicle :
    """docstring"""
    def __int__(self, color, doors, tires):
        """constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires

    def brake(self):
        return "Braking"

    def drive(self):
        return "I'm driving"