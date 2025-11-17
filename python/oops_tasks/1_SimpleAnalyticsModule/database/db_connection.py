class DBConnection:
    
    def __init__(self,connectionString):
        self.connectionString = connectionString
        self.isConnected = False
        
    def connect(self):
        
        print(f"Connecting to the database thru {self.connectionString}...")
        self.isConnected = True
        
    
    def fetchData(self,nums):
        
        if (self.isConnected == False):
            print("First connect to the database!")
            return
        
        print(f"Query : {nums}")
        return [10,20,30,50,35]
    
    def closeConnection(self):
        self.isConnected = False
        print("Closed Connection")