class Airplane:
    def __init__(self, seating_plan):
        self.brand = None
        self.model = None
        self.seating_plan = seating_plan
        
        
    def get_seating_no(self):
        rows, seats = self.get_seating_plan() # touple unpacking
        return len(rows) * len(seats)
    
    def get_seating_plan(self):
        return self.seating_plan
    
    def get_airplane_model(self):
        return self.model
    
    