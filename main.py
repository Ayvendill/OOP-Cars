class AllCars:
    def __init__ (self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return '{} is going'.format(self.name)
    def stop(self):
        return '{} is stoped'.format(self.name)
    def turn(self,direction):
        return '{} returned({})'.format(self.name,direction)


class TownCar(AllCars):
    def name(self):
        return self.name

class SportCar(AllCars):
    def name(self):
        return self.name
    
class WorkCar(AllCars):
   def name(self):
        return self.name

car1 = TownCar(80,"Black","Nissan",False)
car2 = SportCar(320,"Red","Pagani",False)
car3 = WorkCar(60,"Green","Chevrolet",False)


print(car2.stop())