import sys
sys.path.append('C:/Users/kathir/OneDrive/Desktop/TicketBookingSystem/Task11/bean')
from Venue import Venue
sys.path.append('C:/Users/kathir/OneDrive/Desktop/TicketBookingSystem/Task11/service')
sys.path.append('C:/Users/kathir/OneDrive/Desktop/TicketBookingSystem/Task11/exception')
from IBookingSystemServiceProvider import IBookingSystemServiceProvider
from IEventServiceProvider import IEventServiceProvider
from Event import Event
from Customer import Customer
from Booking import Booking 
from EventServiceProviderImpl import EventServiceProviderImpl
from BookingSystemServiceProviderImpl import BookingSystemServiceProviderImpl
from EventServiceProviderImpl import EventNotFoundException
from BookingSystemServiceProviderImpl import InvalidBookingIDException
from BookingSystemRepositoryImpl import BookingSystemRepositoryImpl
from InvalidBookingIDException import InvalidBookingIDException
from EventNotFoundException import EventNotFoundException





if __name__ == "__main__":
    bsr = BookingSystemRepositoryImpl()
    

    
    # if id(EventImpl) == id(BookingImpl):
    #     print("EventImpl and BookingImpl are the same instances.")
    # else:
    #     print("EventImpl and BookingImpl are different instances.")


    while True:
        print("\nAvailable Commands:")
        print("1. create_event")
        print("2. book_tickets")
        print("3. cancel_booking")
        print("4. get_available_seats")
        print("5. get_event_details")
        print("6. calculate_booking_cost")
        print("7. get_booking_details")
        print("8. exit")

        command = input("Enter a command: ").strip()
        try:
            if command == "create_event":
                
                event_name = input("Enter event name: ")
                date = input("Enter event date (YYYY-MM-DD): ")
                time = input("Enter event time (HH:MM): ")
                total_seats = int(input("Enter total seats: "))
                available_seats = int(input("Enter available seats: "))
                ticket_price = float(input("Enter ticket price: "))
                event_type = input("Enter event type (Movie/Sports/Concert): ")
                venue_name = input("Enter venue name: ")
                venue_address = input("Enter venue address: ")
                # venue_id = int(input("Enter Venue id: "))

                venue = Venue(venue_name, venue_address)
                c_event = bsr.create_event(event_name, date, time, total_seats, ticket_price, event_type, venue)
                for event in c_event:
                    print("Event Name:", event.event_name)
                    print("Event Date:", event.event_date)
                    print("Event time: ", event.event_time)
                    print("Total seats: ", event.total_seats)
                    print("Available seats: ", event.available_seats)
                    print("Ticket price: ", event.ticket_price)
                    event_type = event.event_type.value
                    print("EventType: ", event_type)
                    
                    print()

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
                bsr.book_tickets(event_name, num_tickets, array_of_customers)

            elif command == "cancel_booking":
               



                booking_id = int(input("Enter booking ID: "))
                bsr.cancel_booking(booking_id)

            elif command == "get_available_seats":
                print("Total Available Seats:", bsr.getAvailableNoOfTickets())

            elif command == "get_event_details":
                eventslist = bsr.getEventDetails()
                for event in eventslist:
                    # print("Event ID:", event.event_id)
                    print("Event Name:", event.event_name)
                    print("Event Date:", event.event_date)
                    print("Event time: ", event.event_time)
                    # print("Venue name: ", event.venue.venue_name)
                    print("Total seats: ", event.total_seats)
                    print("Ticket price: ", event.ticket_price)
                    event_type = event.event_type.value
                    print("EventType: ", event_type)

                    print()

            elif command == "calculate_booking_cost":
                
                # ticket_price = float(input("Enter ticket price: "))
                
                num_tickets = int(input("Enter number of tickets to book: "))
                

                print(bsr.calculate_booking_cost(num_tickets))  

            elif command == "get_booking_details":

                

                booking_id = int(input("Enter bookingId: "))
                
                bookings = bsr.get_booking_details(booking_id)
                for booking in bookings:
                    print("Event Id: ", booking.event_id)
                    print('Customer Id: ', booking.customer_id)
                    print("Number of Tickets: ", booking.num_tickets)
                    print("Booking Date: ", booking.booking_date)


            elif command == "exit":
                print("Exiting program.")
                break

            else:
                print("Invalid command.")

        except EventNotFoundException as e:
            print("Error:", e)
            print("Please make sure to enter a valid event.")
        except InvalidBookingIDException as e:
            print("Error:", e)
            print("Please make sure to enter a valid booking ID.")
        except AttributeError as e:
            # Handle the AttributeError (equivalent to NullPointerException in Java)
            print(f"AttributeError occurred: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")