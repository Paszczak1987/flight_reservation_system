from pprint import pprint as pp

class Flight:
    def __init__(self, flight_number, airplane):
        self.airplane = airplane
        self.flight_number = flight_number
        rows, seats = self.airplane.get_seating_plan()
        self.seating_plan = [None] + [{letter: None for letter in seats} for _ in rows] # składniowe dummy name
    
    def get_airline(self):
        return self.flight_number[:2]
    
    def get_number(self):
        return self.flight_number[2:]
    
    def get_model(self):
        return self.airplane.get_airplane_model()
    
    def _parse_seat(self, seat):
        letter = seat[-1]
        
        rows, seats = self.airplane.get_seating_plan()
        if letter not in seats:
            raise ValueError(f"Invalid seat letter: {letter}")
        
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid row number: {row_text}")
        
        if row not in rows:
            raise ValueError(f"Row number is out of range: {row}")
        
        return row, letter
    
    def allocate_passenger(self, passenger="Lech K", seat="12C"):
        row, letter = self._parse_seat(seat)
        if self.seating_plan[row][letter] is not None:
            raise ValueError(f"Seat is already taken: {seat}")
        self.seating_plan[row][letter] = passenger
        
    def relocate_passenger(self, seat_from, seat_to):
        row_from, letter_from = self._parse_seat(seat_from)
        if self.seating_plan[row_from][letter_from] is None:
            raise ValueError(f"Seat is not occupied: {seat_from}")
        row_to, letter_to = self._parse_seat(seat_to)
        if self.seating_plan[row_to][letter_to] is not None:
            raise ValueError(f"Seat is already taken: {seat_to}")
        self.seating_plan[row_to][letter_to] = self.seating_plan[row_from][letter_from]
        self.seating_plan[row_from][letter_from] = None
        
        
class Airplane:
    def get_seating_no(self):
        rows, seats = self.get_seating_plan() # touple unpacking
        return len(rows) * len(seats)


class AirbusA380(Airplane):
    @staticmethod
    def get_airplane_model():
        return 'Airbus A380'
    
    @staticmethod
    def get_seating_plan():
        return range(1, 26), 'ABCDEG' # tuple packing


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

f.allocate_passenger("Lech K", "12C")
f.allocate_passenger("Jarosław K", "12E")
f.allocate_passenger("Paweł K", "12A")
f.relocate_passenger("12A", "25G")
# print(f.get_airline())
# print(f.get_number())
# print(f.get_model())
# print(airbus.get_airplane_model())
# print(airbus.get_seating_no())
# print(AirbusA380.get_airplane_model())
pp(f.seating_plan)
