import pyodbc
import csv


# Class for containing SQL functions, mainly used for unittest purpose
class DatabaseConnection:
    def __init__(self):
        self.sql_connection_var = self.connect_sql()
        self.cursor = self.sql_connection_var.cursor()

# Function for connecting to the SQL server
    def connect_sql(self):
        sql_connection_var = pyodbc.connect('Driver={SQL Server};'
                                            'Server=THINOTE20-NHS;'
                                            'Database=CiscoNetworkAutomation;'
                                            'Trusted_Connection=yes;')
        return sql_connection_var

# Function for inserting queries to the SQL server
    def insert_sql_query(self, query_to_run):
        self.cursor.execute(query_to_run)
        self.sql_connection_var.commit()


class ConfigLogClass(DatabaseConnection):

    def __init__(self, edb_test, switch_name_test, config_type_test):
        DatabaseConnection.__init__(self)
        self.edb_test = edb_test
        self.switch_name_test = switch_name_test
        self.config_type_test = config_type_test

    def config_log_select(self):
        query = "SELECT Timestamp, Switch_Name, ConfigType FROM dbo.Config_Log WHERE Timestamp =" + " " + str(self.edb_test) + " AND Switch_Name = " + str(self.switch_name_test) + " AND ConfigType = " + str(self.config_type_test)
        row = self.insert_sql_query(query)
        return row

    def config_log_insert(self):
        query = "INSERT INTO dbo.Config_Log (Timestamp,Switch_Name,ConfigType) Values (" + str(self.edb_test) + ", '" + str(self.switch_name_test) + "', " + str(self.config_type_test) + ")"
        self.insert_sql_query(query)

    def config_log_delete(self):
        query = "DELETE FROM dbo.Config_Log WHERE Switch_Name =" + " " + str(self.switch_name_test)
        self.insert_sql_query(query)


# Var containing SQL login info
SQLConnection = pyodbc.connect('Driver={SQL Server};'
                               'Server=THINOTE20-NHS;'
                               'Database=CiscoNetworkAutomation;'
                               'Trusted_Connection=yes;')


# Insert a log entry into the Config_Log table
def InsertLog(timestamp, switch_name, config_type):
    global SQLConnection
    cursor = SQLConnection.cursor()
    cursor.execute('INSERT INTO dbo.Config_Log VALUES (?, ?, ?)', (timestamp, switch_name, config_type))
    SQLConnection.commit()


# Clears the Config_Log table
def clearlog():
    global SQLConnection
    cursor = SQLConnection.cursor()
    cursor.execute('DELETE FROM dbo.Config_Log')
    SQLConnection.commit()


# Clears the first 10 log entries
def clearfirst10log_entries():
    global SQLConnection
    cursor = SQLConnection.cursor()
    cursor.execute('DELETE TOP(10) FROM dbo.Config_Log')
    SQLConnection.commit()


# Print the SQL config log
def printsqlconfiglog():
    global SQLConnection
    cursor = SQLConnection.cursor()
    cursor.execute('SELECT * FROM dbo.Config_Log')

    for row in cursor:
        print(row)


# Print the switch config settings stored in the database
def printsqlswitchconfig():
    global SQLConnection
    cursor = SQLConnection.cursor()
    cursor.execute('SELECT * FROM dbo.Switch_Conf')

    for row in cursor:
        print(row)

# Function for collecting SQL SELECT output and converting to a CSV file, used for config source data
def sqltocsv():
    global SQLConnection
    # File name
    fileName = 'SQL_CSV_Export.csv'

    # Cursor to execute query
    cursor = SQLConnection.cursor()

    # Execute SQL query
    cursor.execute('SELECT * FROM dbo.Switch_Conf')

    # Fetch the data returned.
    results = cursor.fetchall()

    # Extract the table headers.
    headers = [i[0] for i in cursor.description]

    # Open CSV file for writing.
    csvFile = csv.writer(open(fileName, 'w', newline=''),
                            delimiter=',', lineterminator='\r\n',
                            quoting=csv.QUOTE_ALL, escapechar='\\')

    # Add the headers and data to the CSV file.
    csvFile.writerow(headers)
    csvFile.writerows(results)

# Close SQL connection
    SQLConnection.close()


# Test of functions
# printsql()
# sqltocsv()
# clearfirst10log_entries()
# clearlog()
