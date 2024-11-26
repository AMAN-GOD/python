import time

class plant:
    def __init__(self, name):
        self.name = name
        self.height = 0
        self.stage = "Seed"
        
    def grow(self,sunlight,water):
        if sunlight & water:
            self.height += 2
            self.update_stage()
            print(f"{self.name} grew! Current height: {self.height} cm, Stage: {self.stage}")
        else:
            print(f"{self.name} couldn't grow! Ensure sunlight and water are provided.")
            
    def update_stage(self):
        if self.height < 5:
            self.stage = "Seedling"
        elif self.height < 15:
            self.stage = "Young plant"
        else:
            self.stage = "Mature plant"
            
    def status(self):
        print(f"{self.name}: Height = {self.height} cm, Stage = {self.stage}")
        
class cactus(plant):
    def grow(self,sunlight,water):
        if sunlight :
            self.height += 1
            self.update_stage()
            print(f"{self.name} grew! Current height: {self.height} cm, Stage: {self.stage}")
        else:
            print(f"{self.name} needs Sunlight to grow")


if __name__ == "__main__":
    sunflower = plant("sunflower")
    cactus = cactus("Cactus")
    
    plant = int(input("Enter the Plant no you want to check growth of:\n 1.sunflower\n 2.Cactus \n"))
    if plant == 1:
        days = int(input("Enter the no of days you wan to show the resuluts of:- "))
        print("🌱 Starting Plant growth simulator🌱")
        for day in range(1,days):
            print(f"\nDay {day}:")
            sunlight = True
            water = day % 2 == 0
            
            print("Sunflower")
            sunflower.grow(sunlight, water)
            sunflower.status()

            time.sleep(1)
    else:
        print("🌱 Starting Plant growth simulator🌱")
        days = int(input("Enter the no of days you wan to show the resuluts of:- "))
        for day in range(1,days):
            print(f"\nA Day {day}:")
            sunlight = True
            water = day % 2 == 0

            print("\nCactus")
            cactus.grow(sunlight,water)
            cactus.status()

            time.sleep(2)
        
