class Building:
    def __init__(self):
        self.construct = []

    def __str__(self):
        return f"Parts of building to be worked out {', ' . join(self.construct)}"
    
 
class BobTheBuilder:
    def __init__(self):
        self.building = Building()

    def add_concrete_on_roof(self):
        self.building.height.append("Roof")
        return self
    
    def fix_pipes(self):
        self.building.height.append("Pipes")
        return self
    
    def add_window(self):
        self.building.height.append("Window")
        return self
    
    def build(self):
        return self.building
    

b = BobTheBuilder().add_concrete_on_roof().fix_pipes().add_window().build()

print(b)
    

