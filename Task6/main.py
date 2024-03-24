from TicketBookingSystemImpl import TicketBookingSystemImpl
from Event_abstracted import Movie
from Event_abstracted import Sports
from Event_abstracted import Concert
ticket_booking_system = TicketBookingSystemImpl()

while True:
    print("1. Create Event")
    print("2. Get Available seats")
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
    
        print(ticket_booking_system.retrieve_available_tickets(event))


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