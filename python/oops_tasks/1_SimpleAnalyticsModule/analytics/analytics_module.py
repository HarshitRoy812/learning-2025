class AnalyticsService:
    
    def __init__(self,db):
        self.db = db
        
    def sum_of_sales(self):
        
        if (self.db):
            
            data = self.db.fetchData("Select sum from orders")

            return sum(data)
        
        
    def avg_of_sales(self):
        
        if (self.db):
            
            data = self.db.fetchData("Select average from orders")

            avg = (sum(data) / len(data))
            
            return avg
        
    
        