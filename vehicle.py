# Parent class
class Vehicle:

    wheels = 4 #class level attribute assigned to every object from the class Vehicle

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    #method that we can perform on the object
    def __str__(self):
        #return a string representing the vehicle object
        return f"Vehicle: {self.make}, Model: {self.model}, Year: {self.year}"
    