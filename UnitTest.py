import unittest
from SQL_Connection import *


class SQLUnitTest(unittest.TestCase):
    sql_connection_class = DatabaseConnection()
    connection = sql_connection_class.connect_sql()

    def test_sql_connection(self):
        connection = DatabaseConnection().connect_sql()
        self.assertIsNotNone(connection)
        connection.close()

    def test_insert_log(self):
        data_to_insert = ConfigLogClass(123, 222, 333)
        data_to_insert.config_log_insert()
        get_log_data = data_to_insert.config_log_select()
        self.assertEqual((data_to_insert.edb_test, data_to_insert.switch_name_test, data_to_insert.config_type_test), (get_log_data.edb_test, get_log_data.switch_name_test, get_log_data.config_type_test))
        data_to_insert.config_log_delete()
        verify_data_delete = data_to_insert.config_log_select()
        self.assertIsNone(verify_data_delete)


if __name__ == '__main__':
    unittest.main()
