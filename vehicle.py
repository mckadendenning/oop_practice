# Parent class
class Vehicle:

    wheels = 4 #class level attribute assigned to every object from the class Vehicle
    all_vehicles = []

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

        Vehicle.all_vehicles.append(self)

    #method that we can perform on the object
    def __str__(self):
        #return a string representing the vehicle object
        return f"Vehicle: {self.make}, Model: {self.model}, Year: {self.year}"
    
    @classmethod
    def get_all_vehicles(cls):
        return cls.all_vehicles
    