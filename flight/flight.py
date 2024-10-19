class Flight:
    def __init__(self, flight_number, airplane):
        self.airplane = airplane
        self.flight_number = flight_number
        rows, seats = self.airplane.get_seating_plan()
        self.seating_plan = [None] + [{letter: None for letter in seats} for _ in rows]  # składniowe dummy name
    
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
    
    def get_empty_seats(self):
        empty_seats = 0
        for value in self.seating_plan[1:]:
            for seat in value.values():
                if seat is None:
                    empty_seats += 1
        return empty_seats
    
    def get_passenger_list(self):
        rows, seats = self.airplane.get_seating_plan()
        for row in rows:
            for letter in seats:
                passenger = self.seating_plan[row][letter]
                if passenger is not None:
                    yield passenger, f'{row}{letter}'

    def get_seating_plan(self):
        return self.seating_plan[1:]
    
    def print_tickets(self, printer):
        for passenger, seat in self.get_passenger_list():
            printer(passenger, seat, self.get_model(), self.flight_number)
    
    def print_seating_plan(self, printer):
        printer(self)
        
    def print_all_passengers(self, printer):
        printer(self)
        
        