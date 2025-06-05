# Full backend logic and Flask UI in one script for Beverage Customization System with calories and size support

from abc import ABC, abstractmethod
from flask import Flask, render_template_string, request

# === Base Beverage Interface ===
class Beverage(ABC):
    def __init__(self, size='Medium'):
        self.size = size

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def calories(self) -> int:
        pass

    def size_multiplier(self):
        return {'Small': 0.9, 'Medium': 1.0, 'Large': 1.2}.get(self.size, 1.0)

# === Concrete Beverages ===
class Espresso(Beverage):
    def get_description(self):
        return f"{self.size} Espresso"

    def cost(self):
        return 2.0 * self.size_multiplier()

    def calories(self):
        return int(5 * self.size_multiplier())

class Tea(Beverage):
    def get_description(self):
        return f"{self.size} Tea"

    def cost(self):
        return 1.5 * self.size_multiplier()

    def calories(self):
        return int(2 * self.size_multiplier())

class Cappuccino(Beverage):
    def get_description(self):
        return f"{self.size} Cappuccino"

    def cost(self):
        return 2.5 * self.size_multiplier()

    def calories(self):
        return int(10 * self.size_multiplier())

# === Abstract Decorator ===
class CondimentDecorator(Beverage, ABC):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage

    def size_multiplier(self):
        return self._beverage.size_multiplier()

# === Concrete Decorators ===
class Milk(CondimentDecorator):
    def get_description(self):
        return self._beverage.get_description() + ", Milk"

    def cost(self):
        return self._beverage.cost() + 0.5 * self.size_multiplier()

    def calories(self):
        return self._beverage.calories() + int(50 * self.size_multiplier())

class Caramel(CondimentDecorator):
    def get_description(self):
        return self._beverage.get_description() + ", Caramel"

    def cost(self):
        return self._beverage.cost() + 0.7 * self.size_multiplier()

    def calories(self):
        return self._beverage.calories() + int(80 * self.size_multiplier())

class Whip(CondimentDecorator):
    def get_description(self):
        return self._beverage.get_description() + ", Whipped Cream"

    def cost(self):
        return self._beverage.cost() + 0.6 * self.size_multiplier()

    def calories(self):
        return self._beverage.calories() + int(60 * self.size_multiplier())

class Chocolate(CondimentDecorator):
    def get_description(self):
        return self._beverage.get_description() + ", Chocolate"

    def cost(self):
        return self._beverage.cost() + 0.8 * self.size_multiplier()

    def calories(self):
        return self._beverage.calories() + int(100 * self.size_multiplier())

# === Flask Web App ===
app = Flask(__name__)

HTML_TEMPLATE = HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Coffee Customizer</title>
    <style>
        body {
            background-color: #000;
            color: #00ff00;
            font-family: 'Courier New', Courier, monospace;
            padding: 30px;
        }
        h2, h3 {
            color: #0f0;
        }
        select, input[type="checkbox"], input[type="submit"] {
            background-color: #111;
            color: #0f0;
            border: 1px solid #0f0;
            padding: 8px;
            margin: 4px 0;
        }
        input[type="submit"] {
            cursor: pointer;
            font-weight: bold;
        }
        form {
            max-width: 400px;
            background-color: #020;
            padding: 20px;
            border: 2px solid #0f0;
            border-radius: 10px;
            box-shadow: 0 0 15px #0f0;
        }
        p {
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <h2>☕ Beverage Builder</h2>
    <form method="post">
        <label>Choose base:</label><br>
        <select name="base">
            <option value="Espresso">Espresso</option>
            <option value="Tea">Tea</option>
            <option value="Cappuccino">Cappuccino</option>
        </select><br><br>

        <label>Size:</label><br>
        <select name="size">
            <option value="Small">Small</option>
            <option value="Medium" selected>Medium</option>
            <option value="Large">Large</option>
        </select><br><br>

        <label>Add condiments:</label><br>
        <input type="checkbox" name="condiments" value="Milk">Milk<br>
        <input type="checkbox" name="condiments" value="Caramel">Caramel<br>
        <input type="checkbox" name="condiments" value="Whip">Whipped Cream<br>
        <input type="checkbox" name="condiments" value="Chocolate">Chocolate<br><br>

        <input type="submit" value="☠ Brew">
    </form>

    {% if description %}
        <h3>🔎 Your Order:</h3>
        <p><strong>Description:</strong> {{ description }}</p>
        <p><strong>Total Cost:</strong> ${{ cost }}</p>
        <p><strong>Total Calories:</strong> {{ calories }} kcal</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def customize():
    description = cost = calories = None
    if request.method == "POST":
        size = request.form["size"]
        base = request.form["base"]
        condiments = request.form.getlist("condiments")

        # Create base beverage
        drink: Beverage
        if base == "Espresso":
            drink = Espresso(size)
        elif base == "Tea":
            drink = Tea(size)
        elif base == "Cappuccino":
            drink = Cappuccino(size)

        # Add condiments
        for item in condiments:
            if item == "Milk":
                drink = Milk(drink)
            elif item == "Caramel":
                drink = Caramel(drink)
            elif item == "Whip":
                drink = Whip(drink)
            elif item == "Chocolate":
                drink = Chocolate(drink)

        description = drink.get_description()
        cost = f"{drink.cost():.2f}"
        calories = drink.calories()

    return render_template_string(HTML_TEMPLATE, description=description, cost=cost, calories=calories)

app.run(debug=False)

