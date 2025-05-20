import json
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Type

@dataclass
class EngineSpec:
    type: str
    power: float

@dataclass
class VehicleSpecs:
    wheels: int
    seats: int
    engine: EngineSpec

class Vehicle(ABC):
    def __init__(self, specs: VehicleSpecs):
        self.specs = specs
    
    @abstractmethod
    def drive(self) -> None:
        pass
    
    def get_specifications(self) -> str:
        return (f"{self.__class__.__name__}: "
                f"{self.specs.wheels} wheels, "
                f"{self.specs.seats} seats, "
                f"{self.specs.engine.type} engine ({self.specs.engine.power}hp)")

class Car(Vehicle):
    def drive(self) -> None:
        print("Driving a car...")

class Motorcycle(Vehicle):
    def drive(self) -> None:
        print("Riding a motorcycle...")

class Truck(Vehicle):
    def drive(self) -> None:
        print("Driving a truck...")

class VehicleFactory:
    def __init__(
        self, 
        vehicle_classes: Dict[str, Type[Vehicle]],
        config_file: str = None
    ):
        self.vehicle_classes = vehicle_classes
        self.config = self._load_config(config_file) if config_file else None
    
    def _load_config(self, config_file: str) -> dict:
        config_path = Path(config_file)
        if not config_path.exists():
            print(f"Warning: Config file {config_file} not found. Using default vehicles.")
            return None
        
        with open(config_path) as f:
            config = json.load(f)
        
        return {k.lower(): v for k, v in config.items()}
    
    def _create_default_vehicle(self, vehicle_type: str) -> Vehicle:
        vehicle_class = self.vehicle_classes.get(vehicle_type.lower())
        if not vehicle_class:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")
        
        defaults = {
            "car": VehicleSpecs(4, 5, EngineSpec("gasoline", 150)),
            "motorcycle": VehicleSpecs(2, 2, EngineSpec("gasoline", 80)),
            "truck": VehicleSpecs(6, 2, EngineSpec("diesel", 300))
        }
        
        return vehicle_class(defaults.get(vehicle_type.lower()))
    
    def create_vehicle(self, vehicle_type: str) -> Vehicle:
        vehicle_type = vehicle_type.lower()
        
        if self.config and vehicle_type in self.config:
            config = self.config[vehicle_type]
            try:
                specs = VehicleSpecs(
                    wheels=config["wheels"],
                    seats=config["seats"],
                    engine=EngineSpec(
                        type=config["engine"]["type"],
                        power=config["engine"]["power"]
                    )
                )
                vehicle_class = self.vehicle_classes.get(config["class"].lower())
                if vehicle_class:
                    return vehicle_class(specs)
            except (KeyError, AttributeError) as e:
                print(f"Invalid config for {vehicle_type}: {e}")
        
        return self._create_default_vehicle(vehicle_type)

if __name__ == "__main__":
    vehicle_classes = {
        "car": Car,
        "motorcycle": Motorcycle,
        "truck": Truck
    }
    
    factory = VehicleFactory(
        vehicle_classes=vehicle_classes,
        config_file="vehicles_config.json"
    )

    print("Vehicle Factory System")
    print("Available vehicle types (try these or others from your JSON):")
    print("- car\n- motorcycle\n- truck\n- hybrid car\n- electric motorcycle")
    
    while True:
        user_input = input("\nEnter vehicle type (or 'quit' to exit): ").strip()
        
        if user_input.lower() == 'quit':
            print("Exiting vehicle factory system...")
            break
        
        try:
            vehicle = factory.create_vehicle(user_input)
            vehicle.drive()
            print(vehicle.get_specifications())
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")