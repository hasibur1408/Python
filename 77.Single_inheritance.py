class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
    def Display(self):
        print(f"Vehicle Name:{self.name} Speed:{self.max_speed} Mileage: {self.mileage}")
        
class Buss(Vehicle):
    def __init__(self,name,max_speed,mileage):
        
        super().__init__(name, max_speed, mileage)
        
    def Display(self):
        print(f"Bus Name:{self.name} Speed:{self.max_speed} Mileage:{self.mileage}")
    
bus=Buss("school volvo",60,12)
bus.Display()
    