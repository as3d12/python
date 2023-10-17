class vehicle:
    def __init__(self,fule,speed=0,make="unknown"):
        self.fule=fule
        self.speed=speed
        self.make=make
        
    def printInfo(self):
        print(f"fule: {self.fule} / speed: {self.speed} / make: {self.make}")
        
    def changeFuel(self,liters):
        self.fule+=liters
        
        
        
class Truck(vehicle):
    def __init__(self,fule,speed,make,cargospace,numberofwheels,cost):
        super().__init__(fule,speed,make)
        self.cargospace=cargospace
        self.numberofwheels=numberofwheels
        self.cost=cost
        
    def printInfo(self):
        super().printInfo()
        print(f"cargospace : {self.cargospace} / numberofwheels: {self.numberofwheels} / cost: {self.cost}")
        
    def getCost(self):
        return self.cost
    
v1=vehicle(300,200,"toyota")
v1.printInfo()
v1.changeFuel(10)
v1.printInfo()
v2=Truck(3000,2000,"tesla",100,4,10000)
v2.printInfo()
v2.getCost()
    
            
        