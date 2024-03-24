from abc import ABC, abstractmethod
import sys
sys.path.append('C:/Users/kathir/OneDrive/Desktop/TicketBookingSystem/Task11/bean')
from Venue import Venue 
class IEventServiceProvider(ABC):
    @abstractmethod
    def create_event(self, event_name: str, date: str, time: str, total_seats: int, ticket_price: float,
                     event_type: str, venue: Venue):
        pass

    @abstractmethod
    def getEventDetails(self):
        pass

    @abstractmethod
    def getAvailableNoOfTickets(self):
        pass