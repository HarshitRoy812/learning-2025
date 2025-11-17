class AC:
    
    def turn_on(self):
        print("AC is on")
        
    def turn_off(self):
        print("AC is off")
        
class TV:
    
    def turn_on(self):
        print("TV is on")
    
    def turn_off(self):
        print("TV is off")
        
class Fan:
    
    def turn_on(self):
        print("Fan is on")
    
    def turn_off(self):
        print("Fan is off")
        
class Remote:
    
    def __init__(self,device):
        self.device = device
        
    def turn_on_device(self):
        self.device.turn_on()
        
    def turn_off_device(self):
        self.device.turn_off()
        
        
ac_remote = Remote(AC())
ac_remote.turn_off_device()

fan_remote = Remote(Fan())
fan_remote.turn_on_device()