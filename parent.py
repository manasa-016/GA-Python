class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(
        self.brand,
        self.model,
        "started"
    )

    def stop(self):
        print(
        self.brand,
        self.model,
        "stopped"
    )

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def drive(self):
        print(
        self.brand,
        self.model,
        "is driving"
        )

    def display(self):
        super().display()
        print("Doors:", self.doors)

        
class Bike(Vehicle):
    def __init__(
    self,
    brand,
    model,
    engine_cc
    ):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    def ride(self):
        print(
        self.brand,
        self.model,
        "is riding"
    )

    def display(self):
        super().display()
        print(
        "Engine:",
        self.engine_cc,
        "cc"
    )
    
class ElectricCar(Car):
    def __init__(
    self,
    brand,
    model,
    doors,
    battery_capacity
    ):
        super().__init__(
        brand,
        model,
        doors
        )
        self.battery_capacity = battery_capacity

    def charge(self):
        print(
        self.brand,
        self.model,
        "is charging"
        )

    def display(self):
        super().display()
        print(
        "Battery:",
        self.battery_capacity,
        "kWh"
        )
car = Car( "Toyota", "Camry", 4 )
bike = Bike( "Honda", "Shine", 125 )
electric_car = ElectricCar( "Tata", "Nexon EV", 4, 40 )

print("===== CAR =====")

car.start() 
car.drive() 
car.display() 
car.stop()

print("\n===== BIKE =====")

bike.start() 
bike.ride() 
bike.display() 
bike.stop()

print("\n===== ELECTRIC CAR =====")

electric_car.start() 
electric_car.drive() 
electric_car.charge() 
electric_car.display() 
electric_car.stop()