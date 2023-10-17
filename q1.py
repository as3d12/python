class vehicle:
    def __init__(self,fule,speed=0,make="unknown"):
        self.fule=fule
        self.speed=speed
        self.make=make
        
    def printInfo(self):
        print("fule:", self.fule)
        print("speed:",self.speed) 
        print("make:",self.make)
        
    def changeFuel(self,liters):
        self.fule+=liters
        
        
        
class Truck(vehicle):
    def __init__(self,fule,speed,make,cargospace,numberofwheels,cost):
        super().__init__(fule,speed,make)
        self.cargospace=cargospace
        self.numberofwheels=numberofwheels
        self.cost=cost
        
    def printInfo(self):
        print("cargospace :", self.cargospace)
        print("numberofwheels:",self.numberofwheels) 
        print("cost:",self.cost)
        
    def getCost(self):
        return self.cost
    
obj1=vehicle(300,200,"toyota")
obj1.printInfo()
obj1.changeFuel(10)
obj1.printInfo()
obj2=Truck(3000,2000,"tesla",100,4,10000)
obj2.printInfo()
obj2.getCost()
    
            
        