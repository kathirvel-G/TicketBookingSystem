from datetime import datetime
from Venue import Venue
from Event import Event, EventType, Movie, Sports, Concert
from Customer import Customer
from Booking import Booking


class BookingSystem:
    def __init__(self):
        self.events = []
        self.bookings = []

    def create_event(self, event_name: str, date: str, time: str, total_seats: int, ticket_price: float,
                     event_type: str, venue: Venue) -> Event:
        
        if event_type == "Movie":
            genre = input('Enter genre: ')
            actor_name = input("Enter actor name: ")
            actress_name = input("Enter actress name: ")
            event = Movie(event_name, date, time, venue_name, total_seats, ticket_price, EventType.Movie, genre, actor_name, actress_name)
        elif event_type == "Sport":
            sport_name = input("sport name: ")
            teams_name = input("teams name: ")
            event = Sports(event_name, date, time, venue_name, total_seats, ticket_price, EventType.Sports, sport_name, teams_name)
        elif event_type == "Concert":
            artist = input("artist name: ")
            concert_type = input("enter concert type: ")
            event = Concert(event_name, date, time, venue_name, total_seats, ticket_price, EventType.Concert, artist, concert_type)
        else:
            raise ValueError("Invalid event type. Supported types are: movie, sport, concert")
        
        print("Event created successfully")
        self.events.append(event)
        print(self.events)
        return event

    def calculate_booking_cost(self, num_tickets, ticket_price):
        return num_tickets * ticket_price

    def book_tickets(self, event_name, num_tickets, array_of_customers):
        for event in self.events:
            if event.event_name == event_name:
                if event.available_seats >= num_tickets:
                    event.book_tickets(num_tickets)
                    booking_date = datetime.now()
                    booking = Booking(array_of_customers, event, num_tickets, booking_date)
                    event.bookings.append(booking)  
                    print(f"{num_tickets} tickets booked for {event_name}.")
                    return  
                    
        print("Event not found or tickets sold out.")


    def cancel_booking(self, booking_id):
        booking_id = int(booking_id)  
        for event in self.events:
            for booking in event.bookings:
                if booking.bookingId == booking_id:
                    
                    print("Cancelled Booking Details:")
                    print("Booking ID:", booking.bookingId)
                    print("Event Name:", event.event_name)
                    print("Event Date:", event.event_date)
                    print("Number of Tickets:", booking.num_tickets)
                    
                    
                    event.cancel_booking(booking.num_tickets)
                    event.bookings.remove(booking)
                    print(f"Booking with ID {booking_id} cancelled.")
                    return
        print("Booking not found.")




    def getAvailableNoOfTickets(self):
        total_available_tickets = 0
        for event in self.events:
            total_available_tickets += event.available_seats
        return total_available_tickets

    def getEventDetails(self):
        for event in self.events:
            event.display_event_details()


if __name__ == "__main__":
    booking_system = BookingSystem()

    while True:
        print("\nAvailable Commands:")
        print("1. create_event")
        print("2. book_tickets")
        print("3. cancel_booking")
        print("4. get_available_seats")
        print("5. get_event_details")
        print("6. exit")

        command = input("Enter a command: ").strip()

        if command == "create_event":
            event_name = input("Enter event name: ")
            date = input("Enter event date (YYYY-MM-DD): ")
            time = input("Enter event time (HH:MM): ")
            total_seats = int(input("Enter total seats: "))
            ticket_price = float(input("Enter ticket price: "))
            event_type = input("Enter event type (Movie/Sports/Concert): ")
            venue_name = input("Enter venue name: ")
            venue_address = input("Enter venue address: ")

            venue = Venue(venue_name, venue_address)
            event = booking_system.create_event(event_name, date, time, total_seats, ticket_price, event_type, venue)

            print(f"Event Name: {event.event_name}")
            print(f"Event Date: {event.event_date}")
            print(f"Event Time: {event.event_time}")
            print(f"Total Seats: {event.total_seats}")
            event_type = event.event_type.value
            print("EventType: ", event_type)
            print(f"Ticket Price: ${event.ticket_price}")
            

            if event_type == "Movie":
                print(f"Genre: {event.genre}")
                print(f"Actor name: {event.actor_name}")
                print(f"Actress name: {event.actress_name}")

            elif event_type == "Sport":
                print(f"Sport Name: {event.sport_name}")
                print(f"Team's name: {event.teams_name}")

            else: 
                print(f"Artist: {event.artist}")
                print(f"Concert Type: {event.concert_type}")

            

        elif command == "book_tickets":

            event_name = input("Enter event name: ")
            num_tickets = int(input("Enter number of tickets to book: "))
            array_of_customers = []
            for i in range(num_tickets):
                customer_name = input("Enter customer name: ")
                email = input("Enter customer email: ")
                phone_number = input("Enter customer phone number: ")
                customer = Customer(customer_name, email, phone_number)
                array_of_customers.append(customer)
            booking_system.book_tickets(event_name, num_tickets, array_of_customers)

        elif command == "cancel_booking":

            booking_id = int(input("Enter booking ID: "))
            booking_system.cancel_booking(booking_id)

        elif command == "get_available_seats":
            print("Total Available Seats:", booking_system.getAvailableNoOfTickets())

        elif command == "get_event_details":
            booking_system.getEventDetails()

        elif command == "exit":
            print("Exiting program.")
            break

        else:
            print("Invalid command.")
