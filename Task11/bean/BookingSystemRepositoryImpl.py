import sys
sys.path.append('C:/Users/kathir/OneDrive/Desktop/TicketBookingSystem/Task11/util')
sys.path.append('C:/Users/kathir/OneDrive/Desktop/TicketBookingSystem/Task11/service')
from typing import List
sys.path.append('C:/Users/kathir/OneDrive/Desktop/TicketBookingSystem/Task11/exception')
from Venue import Venue
from Event import Event
from Customer import Customer
from Booking import Booking
from datetime import datetime
from db_conn_util import DBConnUtil
from IBookingSystemRepository import IBookingSystemRepository
from DatabaseConnectionHandling import DatabaseConnectionError
from DatabaseConnectionHandling import DatabaseQueryError

class BookingSystemRepositoryImpl(IBookingSystemRepository):
    def __init__(self):
        self.conn_util = DBConnUtil()

    def create_event(self, event_name: str, date: str, time: str, total_seats: int, ticket_price: float,
                 event_type: str, venue: Venue) -> Event:
        try:
            venue_id = int(input("Enter venueid: "))
            
            conn = self.conn_util.get_connection()
            cursor = conn.cursor()

            
            sql = """
            INSERT INTO Event (event_name, event_date, event_time, total_seats, available_seats, ticket_price, event_type,venue_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(sql, (event_name, date, time, total_seats, total_seats, ticket_price, event_type, venue_id))
            conn.commit()

            print("Event created successfully")

            
            cursor.execute("SELECT SCOPE_IDENTITY() AS last_id")
            events=[]
            last_id = cursor.fetchone().last_id
            new_event = Event(event_name, date, time, venue, total_seats, ticket_price, event_type)
            events.append(new_event)
            return events 

        
        except pyodbc.Error as e:
            raise DatabaseQueryError("Error creating event: " + str(e))
        except Exception as e:
            raise DatabaseConnectionError("Error connecting to database: " + str(e))
        finally:
            cursor.close()
            conn.close()


    def getEventDetails(self) -> List[Event]:
        try:
            conn = self.conn_util.get_connection()
            cursor = conn.cursor()

            
            sql = """
            SELECT * FROM Event
            """
            cursor.execute(sql)
            events = []

            
            for row in cursor.fetchall():
                event = Event(row[1], row[2], row[3], row[8], row[4], row[6], row[7])
                events.append(event)

            return events

        except pyodbc.Error as e:
            raise DatabaseQueryError("Error fetching event details: " + str(e))
        except Exception as e:
            raise DatabaseConnectionError("Error connecting to database: " + str(e))
            

        finally:
            cursor.close()
            conn.close()

    def getAvailableNoOfTickets(self) -> int:
        try:
            conn = self.conn_util.get_connection()
            cursor = conn.cursor()

            
            sql = """
            SELECT SUM(available_seats) FROM Event
            """
            cursor.execute(sql)
            total_tickets = cursor.fetchone()[0]

            return total_tickets

        except pyodbc.Error as e:
            raise DatabaseQueryError("Error fetching available tickets: " + str(e))
        except Exception as e:
            raise DatabaseConnectionError("Error connecting to database: " + str(e))

        finally:
            cursor.close()
            conn.close()

    def calculate_booking_cost(self, num_tickets: int) -> float:
        try:
            conn = self.conn_util.get_connection()
            cursor = conn.cursor()
            event_id = int(input("Enter eventid: "))

            
            sql = "SELECT ticket_price FROM Event WHERE event_id = ?"
            cursor.execute(sql, (event_id,))
            row = cursor.fetchone()

            if row:
                ticket_price = row[0]
                total_cost = ticket_price * num_tickets
                return total_cost
            else:
                print("Event not found.")
                return None

        except pyodbc.Error as e:
            raise DatabaseQueryError("Error calculating booking cost: " + str(e))
        except Exception as e:
            raise DatabaseConnectionError("Error connecting to database: " + str(e))
        

        finally:
            cursor.close()
            conn.close()



    def book_tickets(self, event_name: str, num_tickets: int, list_of_customers: List[Customer]):
        try:
            conn = self.conn_util.get_connection()
            cursor = conn.cursor()

            
            sql_event = "SELECT event_id, available_seats, ticket_price FROM Event WHERE event_name = ?"
            cursor.execute(sql_event, (event_name,))
            row = cursor.fetchone()

            if row:
                event_id, available_seats, ticket_price = row
                if available_seats < num_tickets:
                    print("Not enough available seats.")
                    return False

                
                updated_seats = available_seats - num_tickets
                sql_update_seats = "UPDATE Event SET available_seats = ? WHERE event_id = ?"
                cursor.execute(sql_update_seats, (updated_seats, event_id))

                total_cost = ticket_price * num_tickets
                booking_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                
                for customer in list_of_customers:
                    
                    sql_insert_customer = "INSERT INTO Customer (customer_name, email, phone_number) VALUES (?, ?, ?)"
                    cursor.execute(sql_insert_customer, (customer.customer_name, customer.email, customer.phone_number))
                    
                    
                    cursor.execute("SELECT @@IDENTITY AS id")
                    customer_id = cursor.fetchone()[0]

                    sql_insert_booking = "INSERT INTO Booking (num_tickets, total_cost, booking_date, event_id, customer_id) VALUES (?, ?, ?, ?, ?)"
                    cursor.execute(sql_insert_booking, (num_tickets, total_cost, booking_date, event_id, customer_id))

                    cursor.execute("SELECT @@IDENTITY AS id")
                    booking_id = cursor.fetchone()[0]

                    sql_update_booking_id = "UPDATE Event SET booking_id = ? WHERE event_id = ?"
                    cursor.execute(sql_update_booking_id, (booking_id, event_id))

                    sql_updatebookingid = "UPDATE Customer SET booking_id = ? WHERE customer_id = ?"
                    cursor.execute(sql_updatebookingid, (booking_id, customer_id))

                conn.commit()
                print(f"{num_tickets} tickets booked for {event_name}.")
                return True

            else:
                print("Event not found.")
                return False

        except pyodbc.Error as e:
            raise DatabaseQueryError("Error booking tickets: " + str(e))
        except Exception as e:
            raise DatabaseConnectionError("Error connecting to database: " + str(e))

        finally:
            cursor.close()
            conn.close()



    def cancel_booking(self, booking_id: int):
        try:
            conn = self.conn_util.get_connection()
            cursor = conn.cursor()

            
            sql_booking = "SELECT event_id, num_tickets FROM Booking WHERE booking_id = ?"
            cursor.execute(sql_booking, (booking_id,))
            booking_row = cursor.fetchone()

            if booking_row:
                event_id, num_tickets = booking_row

                
                sql_update_seats = "UPDATE Event SET available_seats = available_seats + ? WHERE event_id = ?"
                cursor.execute(sql_update_seats, (num_tickets, event_id))

                

                conn.commit()
                print(f"Booking with ID {booking_id} cancelled.")
                return True
            else:
                print("Booking not found.")
                return False

        except pyodbc.Error as e:
            raise DatabaseQueryError("Error cancelling booking: " + str(e))
        except Exception as e:
            raise DatabaseConnectionError("Error connecting to database: " + str(e))

        finally:
            cursor.close()
            conn.close()

    def get_booking_details(self, booking_id: int):
        try:
            conn = self.conn_util.get_connection()
            cursor = conn.cursor()
            

           
            sql_booking = "SELECT * FROM Booking WHERE booking_id = ?"
            cursor.execute(sql_booking, (booking_id,))
            bookings = []
            for row in cursor.fetchall():
                booking = Booking(row[5], row[4], row[1], row[3])
                bookings.append(booking)
            if bookings:
                return bookings 
            else:
                print("Booking not found.")
                return None

        except pyodbc.Error as e:
            raise DatabaseQueryError("Error fetching booking details: " + str(e))
        except Exception as e:
            raise DatabaseConnectionError("Error connecting to database: " + str(e))

        finally:
            cursor.close()
            conn.close()


