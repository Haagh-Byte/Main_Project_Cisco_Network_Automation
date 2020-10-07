import unittest
from SQL_Connection import *


# Class for unit test
class SQLUnitTest(unittest.TestCase):
    sql_connection_class = DatabaseConnection()
    connection = sql_connection_class.connect_sql()

# Unit test for SQL Connection
    def test_sql_connection(self):
        connection = DatabaseConnection().connect_sql()
        self.assertIsNotNone(connection)
        connection.close()


# Run unit test
if __name__ == '__main__':
    unittest.main()
