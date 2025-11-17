class Coffee:
    
    def brew(self):
        print("Coffee is brewing")
        
class MilkCoffee:
    
    def __init__(self,coffee):
        self.coffee = coffee
        
    def brew(self):
        self.coffee.brew()
        print("Added milk , now milk coffee is brewed")
        
class CaramelCoffee:
    
    def __init__(self,coffee):
        self.coffee = coffee
        
    def brew(self):
        self.coffee.brew()
        print("Now caramel coffee is ready")
        
    
coffee = Coffee()
coffee = MilkCoffee(coffee)
coffee = CaramelCoffee(coffee)

coffee.brew()