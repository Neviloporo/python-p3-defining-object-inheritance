class Vehicle:
    def __init__(self, wheel_size, color, wheel_number=4):
        self.wheel_size = wheel_size
        self.color = color
        self.wheel_number = wheel_number

    def go(self):
        return "vrrrrrrrooom!"
    
    def fill_up_tank(self):
        return "filling up!"

