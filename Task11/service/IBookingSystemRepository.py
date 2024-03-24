from abc import ABC, abstractmethod
from typing import List
from Venue import Venue
from Event import Event
from Customer import Customer
from Booking import Booking
from datetime import datetime


class IBookingSystemRepository(ABC):
    @abstractmethod
    def create_event(self, event_name: str, date: str, time: str, total_seats: int, ticket_price: float,
                     event_type: str, venue: Venue) -> Event:
        pass

    @abstractmethod
    def getEventDetails(self) -> List[Event]:
        pass

    @abstractmethod
    def getAvailableNoOfTickets(self) -> int:
        pass

    @abstractmethod
    def calculate_booking_cost(self, num_tickets: int) -> float:
        pass

    @abstractmethod
    def book_tickets(self, event_name: str, num_tickets: int, list_of_customers: List[Customer]) -> Booking:
        pass

    @abstractmethod
    def cancel_booking(self, booking_id: int):
        pass

    @abstractmethod
    def get_booking_details(self, booking_id: int) -> Booking:
        pass

