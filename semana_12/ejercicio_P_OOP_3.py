class Vehicle:
    def __init__(self, model, color, serial_number):
        self.model = model
        self.color = color
        self.serial_number = serial_number

    def start_engine(self):
        print(f"{self.model} Engine started.")

    def stop_engine(self):
        print(f"{self.model} Engine stopped.")

class FuelPowered:
    def refuel(self):
        print("Refueling...")

class ElectricPowered:
    def recharge(self):
        print("Recharging...")

class HybridVehicle(Vehicle, FuelPowered, ElectricPowered):
    def __init__(self, model, color, serial_number, fuel_type):
        super().__init__(model, color, serial_number)
        self.fuel_type = fuel_type

vehicle = HybridVehicle("Toyota Prius", "White", "BQJ582", "Gasoline")
vehicle.start_engine()
vehicle.refuel()
vehicle.recharge()
vehicle.stop_engine()