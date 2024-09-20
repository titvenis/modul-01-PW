class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        pass

    def stop_engine(self):
        pass

class Car(Vehicle):
    def __init__(self, make, model, year, doors, transmission):
        super().__init__(make, model, year)
        self.doors = doors
        self.transmission = transmission

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, body_type, has_sidecar):
        super().__init__(make, model, year)
        self.body_type = body_type
        self.has_sidecar = has_sidecar

class Garage:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle):
        self.vehicles.remove(vehicle)

class Fleet:
    def __init__(self):
        self.garages = []

    def add_garage(self, garage):
        self.garages.append(garage)

    def remove_garage(self, garage):
        self.garages.remove(garage)

    def find_vehicle(self, make, model):
        for garage in self.garages:
            for vehicle in garage.vehicles:
                if vehicle.make == make and vehicle.model == model:
                    return vehicle
        return None
