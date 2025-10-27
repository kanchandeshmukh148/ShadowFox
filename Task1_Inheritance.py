# Base class
class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def make_call(self):
        print("Making a call...")

    def receive_call(self):
        print("Receiving a call...")

    def take_a_picture(self):
        print(f"Taking a picture with {self.rear_camera} rear camera.")


# Apple child class
class Apple(MobilePhone):
    def __init__(self, model, front_camera, rear_camera, ram, storage):
        super().__init__("Touch Screen", "5G", False, front_camera, rear_camera, ram, storage)
        self.model = model

    def show_details(self):
        print(f"Apple Model: {self.model}")
        print(f"Front Camera: {self.front_camera}")
        print(f"Rear Camera: {self.rear_camera}")
        print(f"RAM: {self.ram}")
        print(f"Storage: {self.storage}")


# Samsung child class
class Samsung(MobilePhone):
    def __init__(self, model, dual_sim, front_camera, rear_camera, ram, storage):
        super().__init__("Touch Screen", "4G/5G", dual_sim, front_camera, rear_camera, ram, storage)
        self.model = model

    def show_details(self):
        print(f"Samsung Model: {self.model}")
        print(f"Front Camera: {self.front_camera}")
        print(f"Rear Camera: {self.rear_camera}")
        print(f"RAM: {self.ram}")
        print(f"Storage: {self.storage}")


# Creating Apple objects
apple1 = Apple("iPhone 13", "12MP", "48MP", "4GB", "128GB")
apple2 = Apple("iPhone 14", "16MP", "48MP", "6GB", "256GB")

# Creating Samsung objects
samsung1 = Samsung("Galaxy S21", True, "12MP", "32MP", "8GB", "128GB")
samsung2 = Samsung("Galaxy A52", True, "8MP", "16MP", "6GB", "64GB")

# Using the methods
apple1.show_details()
apple1.take_a_picture()
apple1.make_call()

print()

samsung1.show_details()
samsung1.receive_call()
