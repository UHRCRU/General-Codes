from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, List, Optional

class MealComponentType(Enum):
    MAIN = auto()
    SIDE = auto()
    DRINK = auto()
    DESSERT = auto()
    ADDON = auto()

@dataclass
class MealComponent:
    name: str
    price: float
    calories: int
    component_type: MealComponentType

    def __str__(self):
        return f"{self.name} (${self.price:.2f}, {self.calories} cal)"

class Meal:
    def __init__(self):
        self.components: Dict[MealComponentType, List[MealComponent]] = {
            MealComponentType.MAIN: [],
            MealComponentType.SIDE: [],
            MealComponentType.DRINK: [],
            MealComponentType.DESSERT: [],
            MealComponentType.ADDON: []
        }
        self._total_price = 0.0
        self._total_calories = 0

    def add_component(self, component: MealComponent):
        self.components[component.component_type].append(component)
        self._total_price += component.price
        self._total_calories += component.calories

    def get_total_price(self) -> float:
        return self._total_price

    def get_total_calories(self) -> int:
        return self._total_calories

    def __str__(self):
        parts = []
        for component_type, items in self.components.items():
            if items and component_type != MealComponentType.ADDON:
                parts.append(f"{component_type.name.title()}: {', '.join(str(i) for i in items)}")
        
        if self.components[MealComponentType.ADDON]:
            parts.append(f"Add-ons: {', '.join(str(i) for i in self.components[MealComponentType.ADDON])}")
        
        parts.append(f"TOTAL: ${self.get_total_price():.2f}, {self.get_total_calories()} calories")
        return "\n".join(parts)

class MealBuilder(ABC):
    def __init__(self):
        self._meal = Meal()
        self._components: Dict[MealComponentType, List[MealComponent]] = {
            MealComponentType.MAIN: [],
            MealComponentType.SIDE: [],
            MealComponentType.DRINK: [],
            MealComponentType.DESSERT: [],
            MealComponentType.ADDON: []
        }

    def _load_components(self):
        """Load available components for this builder"""
        pass

    def add_main(self, choice: Optional[int] = None) -> 'MealBuilder':
        if not self._components[MealComponentType.MAIN]:
            self._load_components()
        main = self._components[MealComponentType.MAIN][choice or 0]
        self._meal.add_component(main)
        return self

    def add_side(self, choice: Optional[int] = None) -> 'MealBuilder':
        if not self._components[MealComponentType.SIDE]:
            self._load_components()
        side = self._components[MealComponentType.SIDE][choice or 0]
        self._meal.add_component(side)
        return self

    def add_drink(self, choice: Optional[int] = None) -> 'MealBuilder':
        if not self._components[MealComponentType.DRINK]:
            self._load_components()
        drink = self._components[MealComponentType.DRINK][choice or 0]
        self._meal.add_component(drink)
        return self

    def add_dessert(self, choice: Optional[int] = None) -> 'MealBuilder':
        if not self._components[MealComponentType.DESSERT]:
            self._load_components()
        dessert = self._components[MealComponentType.DESSERT][choice or 0]
        self._meal.add_component(dessert)
        return self

    def add_addon(self, choice: int) -> 'MealBuilder':
        if not self._components[MealComponentType.ADDON]:
            self._load_components()
        addon = self._components[MealComponentType.ADDON][choice]
        self._meal.add_component(addon)
        return self

    def get_meal(self) -> Meal:
        return self._meal

class KidsMealBuilder(MealBuilder):
    def _load_components(self):
        self._components[MealComponentType.MAIN] = [
            MealComponent("Mini Burger", 3.99, 350, MealComponentType.MAIN)
        ]
        self._components[MealComponentType.SIDE] = [
            MealComponent("Small Fries", 1.99, 200, MealComponentType.SIDE)
        ]
        self._components[MealComponentType.DRINK] = [
            MealComponent("Juice Box", 1.49, 120, MealComponentType.DRINK)
        ]
        self._components[MealComponentType.DESSERT] = [
            MealComponent("Mini Ice Cream", 1.99, 150, MealComponentType.DESSERT)
        ]
        self._components[MealComponentType.ADDON] = [
            MealComponent("Toy", 0.99, 0, MealComponentType.ADDON)
        ]

class PremiumMealBuilder(MealBuilder):
    def _load_components(self):
        self._components[MealComponentType.MAIN] = [
            MealComponent("Double Cheeseburger", 6.99, 750, MealComponentType.MAIN),
            MealComponent("Grilled Chicken Sandwich", 7.49, 550, MealComponentType.MAIN)
        ]
        self._components[MealComponentType.SIDE] = [
            MealComponent("Large Fries", 2.99, 400, MealComponentType.SIDE),
            MealComponent("Onion Rings", 3.49, 450, MealComponentType.SIDE)
        ]
        self._components[MealComponentType.DRINK] = [
            MealComponent("Craft Beer", 5.99, 200, MealComponentType.DRINK),
            MealComponent("Premium Soda", 2.49, 180, MealComponentType.DRINK)
        ]
        self._components[MealComponentType.DESSERT] = [
            MealComponent("Cheesecake", 4.99, 600, MealComponentType.DESSERT),
            MealComponent("Chocolate Lava Cake", 5.49, 700, MealComponentType.DESSERT)
        ]
        self._components[MealComponentType.ADDON] = [
            MealComponent("Extra Cheese", 0.99, 100, MealComponentType.ADDON),
            MealComponent("Bacon", 1.49, 150, MealComponentType.ADDON)
        ]

class CustomMealBuilder(MealBuilder):
    def _load_components(self):

        self._components[MealComponentType.MAIN] = [
            MealComponent("Hamburger", 4.99, 500, MealComponentType.MAIN),
            MealComponent("Cheeseburger", 5.49, 550, MealComponentType.MAIN),
            MealComponent("Veggie Burger", 5.99, 400, MealComponentType.MAIN)
        ]
        self._components[MealComponentType.SIDE] = [
            MealComponent("Medium Fries", 2.49, 300, MealComponentType.SIDE),
            MealComponent("Side Salad", 3.99, 150, MealComponentType.SIDE)
        ]
        self._components[MealComponentType.DRINK] = [
            MealComponent("Soda", 1.99, 150, MealComponentType.DRINK),
            MealComponent("Iced Tea", 1.99, 50, MealComponentType.DRINK),
            MealComponent("Bottled Water", 1.49, 0, MealComponentType.DRINK)
        ]
        self._components[MealComponentType.DESSERT] = [
            MealComponent("Cookie", 1.49, 200, MealComponentType.DESSERT),
            MealComponent("Brownie", 2.49, 350, MealComponentType.DESSERT)
        ]
        self._components[MealComponentType.ADDON] = [
            MealComponent("Extra Sauce", 0.49, 50, MealComponentType.ADDON),
            MealComponent("Avocado", 1.99, 100, MealComponentType.ADDON)
        ]

class MealDirector:
    @staticmethod
    def construct_kids_meal() -> Meal:
        builder = KidsMealBuilder()
        return (builder
                .add_main()
                .add_side()
                .add_drink()
                .add_dessert()
                .get_meal())

    @staticmethod
    def construct_premium_meal() -> Meal:
        builder = PremiumMealBuilder()
        return (builder
                .add_main(0) 
                .add_side(1)  
                .add_drink(0) 
                .add_dessert(1)  
                .add_addon(0)  
                .get_meal())

    @staticmethod
    def construct_custom_meal(choices: Dict[str, int]) -> Meal:
        builder = CustomMealBuilder()
        return (builder
                .add_main(choices.get('main', 0))
                .add_side(choices.get('side', 0))
                .add_drink(choices.get('drink', 0))
                .add_dessert(choices.get('dessert', 0))
                .get_meal())

def build_custom_meal_interactively():
    print("\n=== Custom Meal Builder ===")
    builder = CustomMealBuilder()
    builder._load_components()  
    
    meal = Meal()  
    
    for component_type in MealComponentType:
        if component_type == MealComponentType.ADDON:
            continue  
        
        options = builder._components[component_type]
        print(f"\nChoose your {component_type.name.lower()}:")
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        
        while True:
            try:
                choice = int(input("Enter your choice (number): ")) - 1
                if 0 <= choice < len(options):
                    selected = options[choice]
                    meal.add_component(selected)
                    break
                print("Invalid choice, try again.")
            except ValueError:
                print("Please enter a number.")
    
    print("\nAvailable add-ons (optional):")
    addons = builder._components[MealComponentType.ADDON]
    for i, addon in enumerate(addons):
        print(f"{i+1}. {addon}")
    print("0. No add-ons")
    
    while True:
        try:
            addon_choice = int(input("Enter add-on choice (0 to skip): "))
            if addon_choice == 0:
                break
            if 1 <= addon_choice <= len(addons):
                selected_addon = addons[addon_choice - 1]
                meal.add_component(selected_addon)
                print(f"Added {selected_addon.name}")
                break
            print("Invalid choice, try again.")
        except ValueError:
            print("Please enter a number.")
    
    return meal

if __name__ == "__main__":
    print("=== Kids Meal ===")
    kids_meal = MealDirector.construct_kids_meal()
    print(kids_meal)

    print("\n=== Premium Meal ===")
    premium_meal = MealDirector.construct_premium_meal()
    print(premium_meal)

    custom_meal = build_custom_meal_interactively()
    print("\n=== Your Custom Meal ===")
    print(custom_meal)