# Parent class
class Vehicle:

    wheels = 4 #class level attribute assigned to every object from the class Vehicle

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
