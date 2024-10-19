def card_printer(passenger, seat, airplane, flight_number):
    message = f"| Passenger: \033[91m{passenger.title()}\033[0m, seat: {seat}, airplane: {airplane}, {flight_number} |"
    frame = f"+{'-' * (len(message) - 11)}+"
    empty_frame = f"|{' ' * (len(message) - 11)}|"
    
    banner = [frame, empty_frame, message, empty_frame, frame]
    print("\n".join(banner))


def plan_printer(flight):
    longest_passenger = max([len(passenger[0]) for passenger in flight.get_passenger_list()])
    row_no = 1
    for row in flight.get_seating_plan():
        line = ""
        for letter, client in row.items():
            line += f"{letter}: {str(client).center(longest_passenger)} "
        print(f"{str(row_no).rjust(2)}: {line}")
        row_no += 1


def passenger_printer(flight):
    for passenger in flight.get_passenger_list():
        name, seat = passenger
        print(f"{name} {seat}")