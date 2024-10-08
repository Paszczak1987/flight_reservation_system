class Flight:
    def __init__(self, flight_number, airplane):
        self.airplane = airplane
        self.flight_number = flight_number
        
    def get_airline(self):
        return self.flight_number[:2]
    
    def get_number(self):
        return self.flight_number[2:]
    
    def get_model(self):
        return self.airplane.get_airplane_model()

    
class Airplane:
    def get_seating_no(self):
        rows, seats = self.get_seating_plan()
        return len(rows) * len(seats)

class AirbusA380(Airplane):
    @staticmethod
    def get_airplane_model():
        return 'Airbus A380'
    
    @staticmethod
    def get_seating_plan():
        return range(1, 26), 'ABCDEG'

class Boeing737Max(Airplane):
    @staticmethod
    def get_airplane_model():
        return 'Airbus 737 Max'
    
    @staticmethod
    def get_seating_plan():
        return range(1, 46), 'ABCDEGHJK'


airbus = AirbusA380()
boeing = Boeing737Max()
f = Flight('L0127', airbus)

print(f.get_airline())
print(f.get_number())
print(f.get_model())
print(airbus.get_airplane_model())
print(airbus.get_seating_no())
print(AirbusA380.get_airplane_model())


