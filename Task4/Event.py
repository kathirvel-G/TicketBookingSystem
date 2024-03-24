from datetime import datetime

from enum import Enum

class EventType(Enum):
    Movie = 'Movie'
    Sports = 'Sports'
    Concert = 'Concert'

class Event:
    def __init__(self, event_name, event_date, event_time, venue_name, total_seats, ticket_price, event_type):
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.venue_name = venue_name
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.ticket_price = ticket_price
        self.event_type = EventType(event_type) 

    def get_event_name(self):
        return self.event_name

    def set_event_name(self, event_name):
        self.event_name = event_name

    def get_event_date(self):
        return self.event_date

    def set_event_date(self, event_date):
        self.event_date = event_date

    def get_event_time(self):
        return self.event_time

    def set_event_time(self, event_time):
        self.event_time = event_time

    def get_venue_name(self):
        return self.venue_name

    def set_venue_name(self, venue_name):
        self.venue_name = venue_name

    def get_total_seats(self):
        return self.total_seats

    def set_total_seats(self, total_seats):
        self.total_seats = total_seats

    def get_available_seats(self):
        return self.available_seats

    def set_available_seats(self, available_seats):
        self.available_seats = available_seats

    def get_ticket_price(self):
        return self.ticket_price

    def set_ticket_price(self, ticket_price):
        self.ticket_price = ticket_price

    def get_event_type(self):
        return self.event_type

    def set_event_type(self, event_type):
        self.event_type = event_type
    

    
    def calculate_total_revenue(self):
        return self.ticket_price * (self.total_seats - self.available_seats)
    
    def get_booked_no_of_tickets(self):
        return self.total_seats - self.available_seats
    
    def book_tickets(self, num_tickets):
        if num_tickets <= self.available_seats:
            self.available_seats -= num_tickets
            print(f"{num_tickets} tickets booked successfully for {self.event_name}.")
        else:
            print("Not enough seats available to book the requested number of tickets.")
    
    def cancel_booking(self, num_tickets):
        if num_tickets <= (self.total_seats - self.available_seats):
            self.available_seats += num_tickets
            print(f"{num_tickets} tickets cancelled successfully for {self.event_name}.")
        else:
            print("Invalid number of tickets to cancel.")
    
    def display_event_details(self):
        details = ""
        details += f"Event Name: {self.event_name}\n"
        details += f"Date: {self.event_date}\n"
        details += f"Time: {self.event_time}\n"
        details += f"Venue: {self.venue_name}\n"
        details += f"Total Seats: {self.total_seats}\n"
        details += f"Available Seats: {self.available_seats}\n"
        details += f"Ticket Price: {self.ticket_price}\n"
        details += f"Event Type: {self.event_type.value}\n"
        return details







    



































# Example usage:

# event = Event("Movie Night", datetime.now(), datetime.now().strftime("%H:%M"), "ABC Theater", 100, 10, "Movie")
# event.display_event_details()
# event.book_tickets(5)
# event.display_event_details()
# event.cancel_booking(2)
# event.display_event_details()
# print("Total Revenue:", event.calculate_total_revenue())
