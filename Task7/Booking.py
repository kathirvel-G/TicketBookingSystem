from Venue import Venue
from Event import Event
from Customer import Customer
from datetime import datetime

class Booking:
    bookingId_counter = 0

    def __init__(self, customers, event, num_tickets, booking_date):
        self.bookingId = Booking.bookingId_counter
        Booking.bookingId_counter += 1
        self.customers = customers
        self.event = event
        self.num_tickets = num_tickets
        self.total_cost = event.ticket_price * num_tickets
        self.booking_date = booking_date

    def display_booking_details(self):
        print("Booking ID:", self.bookingId)
        print("Booking Date:", self.booking_date)
        print("Event Details:")
        self.event.display_event_details()
        print("Number of Tickets:", self.num_tickets)
        print("Total Cost:", self.total_cost)
        print("Customers:")
        for customer in self.customers:
            customer.display_customer_details()

