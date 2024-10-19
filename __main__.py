from flight import Flight
from planes import Airbus, Boeing
from helpers import *

def main():
    airbus = Airbus('A380', (range(1, 46), 'ABCDEGHJK'))
    boeing = Boeing('737Max', (range(1, 31), 'ABCDEG'))
    
    flight_lo127 = Flight('L0127', airbus)
    
    flight_lo127.allocate_passenger("Lech K", "12C")
    flight_lo127.allocate_passenger("Jarosław K", "12E")
    flight_lo127.allocate_passenger("Paweł K", "12A")
    flight_lo127.relocate_passenger("12A", "25G")
    flight_lo127.allocate_passenger("Łukasz P", "20A")
    flight_lo127.allocate_passenger("Anita G", "20B")
    flight_lo127.allocate_passenger("Lidia G", "20C")
    
    
    flight_lo127.print_seating_plan(plan_printer)
    flight_lo127.print_tickets(card_printer)
    flight_lo127.print_all_passengers(passenger_printer)
    

if __name__ == "__main__":
    main()
    
    