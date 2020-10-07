import unittest
from SQL_Connection import *


class SQLUnitTest(unittest.TestCase):
    sql_connection_class = DatabaseConnection()
    connection = sql_connection_class.connect_sql()

    def test_sql_connection(self):
        connection = DatabaseConnection().connect_sql()
        self.assertIsNotNone(connection)
        connection.close()


if __name__ == '__main__':
    unittest.main()
