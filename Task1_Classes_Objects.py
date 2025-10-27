# Create Avenger class
class Avenger:
    
    # Constructor
    def __init__(self, name, age, gender, power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.power = power
        self.weapon = weapon
    
    # Function to show info of Avengers
    def show_info(self):
        print(f"\nName: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Super Power: {self.power}")
        print(f"Weapon: {self.weapon}")
        
    # Function to show Avenger's leader
    def is_leader(self):
        if self.name == "Captain America":
            print(f"{self.name} is the leader.")
        else:
            print(f"{self.name} is not the leader.")


# Create Avengers using constructor
avengers = [
    Avenger("Captain America", 100, "Male", "Super Strength", "Shield"),
    Avenger("Iron Man", 48, "Male", "Technology", "Armor"),
    Avenger("Black Widow", 35, "Female", "Superhuman", "Batons"),
    Avenger("Hulk", 40, "Male", "Unlimited Strength", "No Weapon"),
    Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir"),
    Avenger("Hawkeye", 38, "Male", "Fighting Skills", "Bow and Arrows")
]

# Show all Avengers info and their leader
for hero in avengers:
    hero.show_info()
    hero.is_leader()