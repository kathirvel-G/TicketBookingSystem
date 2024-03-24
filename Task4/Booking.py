from Event import Event
from datetime import datetime
class Booking:
    def __init__(self, event, num_tickets, booking_date):
        self.event = event
        self.num_tickets = num_tickets
        self.total_cost = 0
        self.booking_date = booking_date

    def calculate_booking_cost(self):
        self.total_cost = self.event.ticket_price * self.num_tickets

    def book_tickets(self):
        if self.num_tickets <= self.event.available_seats:
            self.event.book_tickets(self.num_tickets)
            self.calculate_booking_cost()
            print(f"{self.num_tickets} tickets booked for {self.event.event_name} on {self.booking_date}.")
        else:
            print("Not enough available seats.")

    def cancel_booking(self):
        self.event.cancel_booking(self.num_tickets)
        print(f"{self.num_tickets} tickets cancelled for {self.event.event_name} on {self.booking_date}.")

    def getAvailableNoOfTickets(self):
        return self.event.available_seats

    def getEventDetails(self):
        return self.event.display_event_details()

if __name__ == "__main__":
    event1 = Event("Movie Night", datetime(2024, 4, 15), "18:00", "Cinema Hall 1", 100, 10.00, "Movie")
    booking1 = Booking(event1, 5, datetime(2024, 4, 10))

    print("Available Tickets before booking:", booking1.getAvailableNoOfTickets())

    print("\nBooking tickets for event1...")
    booking1.book_tickets()
    print("Total Cost:", booking1.total_cost)
    print("Available Tickets after booking:", booking1.getAvailableNoOfTickets())

    print("\nCancelling booking for event1...")
    booking1.cancel_booking()
    print("Available Tickets after cancellation:", booking1.getAvailableNoOfTickets())


    print("\nEvent details:")
    print(booking1.getEventDetails())