class Fridge:
    def __init__(self):
        self.food_items = []

    def add_food(self, food):
        self.food_items.append(food)

    def get_food_by_type(self, food_type):
        return [food for food in self.food_items if food.type == food_type]

class Food:
    def __init__(self, name, type):
        self.name = name
        self.type = type

# Create a new fridge
fridge = Fridge()

# Add some food to the fridge
fridge.add_food(Food("apple", "fruit"))
fridge.add_food(Food("banana", "fruit"))
fridge.add_food(Food("lettuce", "vegetable"))
fridge.add_food(Food("bread", "grain"))

# Get all the fruit from the fridge
fruits = fridge.get_food_by_type("fruit")
print("Fruits:", [food.name for food in fruits])

# Get all the vegetables from the fridge
vegetables = fridge.get_food_by_type("vegetable")
print("Vegetables:", [food.name for food in vegetables])

# Get all the grains from the fridge
grains = fridge.get_food_by_type("grain")
print("Grains:", [food.name for food in grains])


## using a list to store food and related food groups
foods = [    {"name": "apple", "food group": "fruit"},    {"name": "broccoli", "food group": "vegetable"},    {"name": "chicken", "food group": "meat"},    {"name": "brown rice", "food group": "grain"},    {"name": "cheddar cheese", "food group": "dairy"},    {"name": "salmon", "food group": "seafood"},    {"name": "peanut butter", "food group": "protein"},    {"name": "orange juice", "food group": "beverage"}]

#access the data from the list 
print(foods[0]["food group"])  # Outputs: "fruit"
print(foods[3]["food group"])  # Outputs: "grain"

