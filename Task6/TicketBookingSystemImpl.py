import sys 
sys.path.append('C:/Users/kathir/OneDrive/Desktop/TicketBookingSystem/Abstraction')

from Event_abstracted import Event
from Event_abstracted import EventType
from Event_abstracted import Movie
from Event_abstracted import Sports
from Event_abstracted import Concert

class TicketBookingSystemImpl():

    
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

    def retrieve_available_tickets(self, event: Event):
        return event.available_seats 