from Event import Event
from Event import Movie
from Event import Sports
from Event import Concert
from Event import EventType
from abc import ABC, abstractmethod
class BookingSystem(ABC):
    @abstractmethod
    def create_event(self, event_name: str, date: str, time: str, total_seats: int, ticket_price: float,
                     event_type: str, venue_name: str) -> Event:
        pass 

    @abstractmethod
    def display_event_details(self, event: Event):
        pass 
    
    @abstractmethod
    def book_tickets(self, event: Event, num_tickets: int) -> float:
        pass

    @abstractmethod
    def cancel_tickets(self, event: Event, num_tickets: int):
        pass

    @abstractmethod
    def retrieve_available_tickets(self):
        pass