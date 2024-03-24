from Event import Event
from Event import Movie
from Event import Sports
from Event import Concert
from Event import EventType
class TicketBookingSystem:
    def create_event(self, event_name: str, date: str, time: str, total_seats: int, ticket_price: float,
                     event_type: str, venue_name: str) -> Event:
       
        if event_type == "movie":
            genre = input('Enter genre: ')
            actor_name = input("Enter actor name: ")
            actress_name = input("Enter actress name: ")
            event = Movie(event_name, date, time, venue_name, total_seats, ticket_price, EventType.Movie, genre, actor_name, actress_name)
        elif event_type == "sport":
            sport_name = input("sport name: ")
            teams_name = input("teams name: ")
            event = Sports(event_name, date, time, venue_name, total_seats, ticket_price, EventType.Sports, sport_name, teams_name)
        elif event_type == "concert":
            artist = input("artist name: ")
            concert_type = input("enter concert type: ")
            event = Concert(event_name, date, time, venue_name, total_seats, ticket_price, EventType.Concert, artist, concert_type)
        else:
            raise ValueError("Invalid event type. Supported types are: movie, sport, concert")
        
        return event

    def display_event_details(self, event: Event):
        event.display_event_details()

    def book_tickets(self, event: Event, num_tickets: int) -> float:
        if event.available_seats >= num_tickets:
            event.available_seats -= num_tickets
            total_cost = num_tickets * event.ticket_price
            return total_cost
        else:
            print("Sorry, the event is sold out. No tickets available.")
            return 0.0

    def cancel_tickets(self, event: Event, num_tickets: int):
        event.available_seats += num_tickets
        print("Ticket cancelled successfully")
        print("Available tickets are: ")
        return event.available_seats


ticket_booking_system = TicketBookingSystem()

while True:
    print("1. Create Event")
    print("2. View Event Details")
    print("3. Book Tickets")
    print("4. Cancel tickets")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        event_type = input("Enter event type (movie/sport/concert): ")
        event_name = input("Enter event name: ")
        date = input("Enter event date (YYYY-MM-DD): ")
        time = input("Enter event time (HH:MM): ")
        venue_name = input("Enter venue name: ")
        total_seats = int(input("Enter total seats: "))
        ticket_price = float(input("Enter ticket price: "))
        

        event = ticket_booking_system.create_event(event_name, date, time, total_seats, ticket_price, event_type, venue_name)
        print("Event created successfully")

        print(f"Event Name: {event.event_name}")
        print(f"Event Date: {event.event_date}")
        print(f"Event Time: {event.event_time}")
        print(f"Total Seats: {event.total_seats}")
        event_type = event.event_type.value
        print("EventType: ", event_type)
        print(f"Ticket Price: ${event.ticket_price}")
        print(f"Venue: {event.venue_name}")

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

        

        
    elif choice == "2":
        
        ticket_booking_system.display_event_details(event)

    elif choice == "3":
        num_tickets = int(input("Enter number of tickets to book: "))
        total_cost = ticket_booking_system.book_tickets(event, num_tickets)
        print("Total Cost:", total_cost)

    elif choice == "4":
        num_tickets = int(input("Enter number of tickets to cancel: "))
        print(ticket_booking_system.cancel_tickets(event, num_tickets))


    elif choice == "5":
        print("Exiting the ticket booking system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")



