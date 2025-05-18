from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Dict
import uvicorn

class MealComponentType(str, Enum):
    MAIN = "main"
    SIDE = "side"
    DRINK = "drink"
    DESSERT = "dessert"
    ADDON = "addon"

class MealComponent(BaseModel):
    name: str
    price: float
    calories: int
    component_type: MealComponentType

    def __str__(self):
        return f"{self.name} (${self.price:.2f}, {self.calories} cal)"

class Meal(BaseModel):
    components: Dict[MealComponentType, List[MealComponent]] = {
        MealComponentType.MAIN: [],
        MealComponentType.SIDE: [],
        MealComponentType.DRINK: [],
        MealComponentType.DESSERT: [],
        MealComponentType.ADDON: []
    }
    total_price: float = 0.0
    total_calories: int = 0

    def add_component(self, component: MealComponent):
        self.components[component.component_type].append(component)
        self.total_price += component.price
        self.total_calories += component.calories

    def __str__(self):
        parts = []
        for component_type, items in self.components.items():
            if items and component_type != MealComponentType.ADDON:
                parts.append(f"{component_type.value.title()}: {', '.join(str(i) for i in items)}")
        
        if self.components[MealComponentType.ADDON]:
            parts.append(f"Add-ons: {', '.join(str(i) for i in self.components[MealComponentType.ADDON])}")
        
        parts.append(f"TOTAL: ${self.total_price:.2f}, {self.total_calories} calories")
        return "\n".join(parts)

class MealDB:
    def __init__(self):
        self.available_components = {
            "kids": {
                MealComponentType.MAIN: [MealComponent(name="Mini Burger", price=3.99, calories=350, component_type=MealComponentType.MAIN)],
                MealComponentType.SIDE: [MealComponent(name="Small Fries", price=1.99, calories=200, component_type=MealComponentType.SIDE)],
                MealComponentType.DRINK: [MealComponent(name="Juice Box", price=1.49, calories=120, component_type=MealComponentType.DRINK)],
                MealComponentType.DESSERT: [MealComponent(name="Mini Ice Cream", price=1.99, calories=150, component_type=MealComponentType.DESSERT)],
                MealComponentType.ADDON: [MealComponent(name="Toy", price=0.99, calories=0, component_type=MealComponentType.ADDON)]
            },
            "premium": {
                MealComponentType.MAIN: [
                    MealComponent(name="Double Cheeseburger", price=6.99, calories=750, component_type=MealComponentType.MAIN),
                    MealComponent(name="Grilled Chicken Sandwich", price=7.49, calories=550, component_type=MealComponentType.MAIN)
                ],
                MealComponentType.SIDE: [
                    MealComponent(name="Large Fries", price=2.99, calories=400, component_type=MealComponentType.SIDE),
                    MealComponent(name="Onion Rings", price=3.49, calories=450, component_type=MealComponentType.SIDE)
                ],
                MealComponentType.DRINK: [
                    MealComponent(name="Craft Beer", price=5.99, calories=200, component_type=MealComponentType.DRINK),
                    MealComponent(name="Premium Soda", price=2.49, calories=180, component_type=MealComponentType.DRINK)
                ],
                MealComponentType.DESSERT: [
                    MealComponent(name="Cheesecake", price=4.99, calories=600, component_type=MealComponentType.DESSERT),
                    MealComponent(name="Chocolate Lava Cake", price=5.49, calories=700, component_type=MealComponentType.DESSERT)
                ],
                MealComponentType.ADDON: [
                    MealComponent(name="Extra Cheese", price=0.99, calories=100, component_type=MealComponentType.ADDON),
                    MealComponent(name="Bacon", price=1.49, calories=150, component_type=MealComponentType.ADDON)
                ]
            },
            "custom": {
                MealComponentType.MAIN: [
                    MealComponent(name="Hamburger", price=4.99, calories=500, component_type=MealComponentType.MAIN),
                    MealComponent(name="Cheeseburger", price=5.49, calories=550, component_type=MealComponentType.MAIN),
                    MealComponent(name="Veggie Burger", price=5.99, calories=400, component_type=MealComponentType.MAIN)
                ],
                MealComponentType.SIDE: [
                    MealComponent(name="Medium Fries", price=2.49, calories=300, component_type=MealComponentType.SIDE),
                    MealComponent(name="Side Salad", price=3.99, calories=150, component_type=MealComponentType.SIDE)
                ],
                MealComponentType.DRINK: [
                    MealComponent(name="Soda", price=1.99, calories=150, component_type=MealComponentType.DRINK),
                    MealComponent(name="Iced Tea", price=1.99, calories=50, component_type=MealComponentType.DRINK),
                    MealComponent(name="Bottled Water", price=1.49, calories=0, component_type=MealComponentType.DRINK)
                ],
                MealComponentType.DESSERT: [
                    MealComponent(name="Cookie", price=1.49, calories=200, component_type=MealComponentType.DESSERT),
                    MealComponent(name="Brownie", price=2.49, calories=350, component_type=MealComponentType.DESSERT)
                ],
                MealComponentType.ADDON: [
                    MealComponent(name="Extra Sauce", price=0.49, calories=50, component_type=MealComponentType.ADDON),
                    MealComponent(name="Avocado", price=1.99, calories=100, component_type=MealComponentType.ADDON)
                ]
            }
        }
        self.saved_meals = {}

db = MealDB()
app = FastAPI()

class ComponentChoice(BaseModel):
    component_type: MealComponentType
    choice_index: int

class CustomMealRequest(BaseModel):
    choices: List[ComponentChoice]
    addons: Optional[List[int]] = None

class MealResponse(BaseModel):
    description: str
    total_price: float
    total_calories: int
    components: Dict[str, List[str]]

@app.get("/meal-types", response_model=List[str])
async def get_meal_types():
    """Get available meal types"""
    return list(db.available_components.keys())

@app.get("/components/{meal_type}", response_model=Dict[str, List[MealComponent]])
async def get_components(meal_type: str):
    """Get available components for a meal type"""
    if meal_type not in db.available_components:
        raise HTTPException(status_code=404, detail="Meal type not found")
    return db.available_components[meal_type]

@app.post("/meals/kids", response_model=MealResponse)
async def create_kids_meal():
    """Create a predefined kids meal"""
    meal = Meal()
    for component in db.available_components["kids"][MealComponentType.MAIN]:
        meal.add_component(component)
    for component in db.available_components["kids"][MealComponentType.SIDE]:
        meal.add_component(component)
    for component in db.available_components["kids"][MealComponentType.DRINK]:
        meal.add_component(component)
    for component in db.available_components["kids"][MealComponentType.DESSERT]:
        meal.add_component(component)
    
    return format_meal_response(meal)

@app.post("/meals/premium", response_model=MealResponse)
async def create_premium_meal():
    """Create a predefined premium meal"""
    meal = Meal()
    meal.add_component(db.available_components["premium"][MealComponentType.MAIN][0])
    meal.add_component(db.available_components["premium"][MealComponentType.SIDE][1])  
    meal.add_component(db.available_components["premium"][MealComponentType.DRINK][0]) 
    meal.add_component(db.available_components["premium"][MealComponentType.DESSERT][1]) 
    meal.add_component(db.available_components["premium"][MealComponentType.ADDON][0])  
    
    return format_meal_response(meal)

@app.post("/meals/custom", response_model=MealResponse)
async def create_custom_meal(request: CustomMealRequest):
    """Create a custom meal with selected components"""
    meal = Meal()
    
    # Add selected components
    for choice in request.choices:
        if choice.component_type not in db.available_components["custom"]:
            raise HTTPException(status_code=400, detail=f"Invalid component type: {choice.component_type}")
        
        components = db.available_components["custom"][choice.component_type]
        if choice.choice_index < 0 or choice.choice_index >= len(components):
            raise HTTPException(status_code=400, detail=f"Invalid choice index for {choice.component_type}")
        
        meal.add_component(components[choice.choice_index])

    if request.addons:
        addons = db.available_components["custom"][MealComponentType.ADDON]
        for addon_index in request.addons:
            if addon_index < 0 or addon_index >= len(addons):
                raise HTTPException(status_code=400, detail=f"Invalid addon index: {addon_index}")
            meal.add_component(addons[addon_index])
    
    meal_id = len(db.saved_meals) + 1
    db.saved_meals[meal_id] = meal
    
    return format_meal_response(meal)

@app.get("/meals/{meal_id}", response_model=MealResponse)
async def get_meal(meal_id: int):
    """Get a previously created meal"""
    if meal_id not in db.saved_meals:
        raise HTTPException(status_code=404, detail="Meal not found")
    return format_meal_response(db.saved_meals[meal_id])

def format_meal_response(meal: Meal) -> MealResponse:
    """Convert a Meal object to API response format"""
    components = {}
    for component_type, items in meal.components.items():
        if items:
            components[component_type.value] = [str(item) for item in items]
    
    return MealResponse(
        description=str(meal),
        total_price=meal.total_price,
        total_calories=meal.total_calories,
        components=components
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)