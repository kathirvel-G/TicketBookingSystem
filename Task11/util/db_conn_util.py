import pyodbc
from db_property_util import DBPropertyUtil

class DBConnUtil:
    def get_connection(self):
        try:
            connection_string = DBPropertyUtil.get_connection_string()
            connection = pyodbc.connect(connection_string)
            print("Connected Successfully")
            return connection

        except Exception as e:
            print("Connection has failed", e)

