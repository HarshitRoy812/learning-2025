class Restaurant:
    
    def cook_food(self,food_item):
        print(f"{food_item} is being cooked")
        
class Payment:
    
    def pay(self):
        print("Payment authorized successfully")
        
class Delivery:
    
    def contact_deliverypartner(self):
        print("Delivery driver is being contacted ...")
        
        
class OrderFood:
    
    def __init__(self,food):
        self.food = food
        
        self.restaurant = Restaurant()
        self.payment = Payment()
        self.delivery = Delivery()
        
    def order_food(self):
        
        self.restaurant.cook_food(self.food)
        self.payment.pay()
        self.delivery.contact_deliverypartner()
        
        print(f"Your {self.food} is ready to be delivered!")
        
food = OrderFood("Pasta")
food.order_food()
        
        
