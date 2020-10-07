import os
from jinja2 import Template
from netmiko import ConnectHandler
from SQL_Connection import *
from Connection_Functions import *

# Function for cleaning up temp files, used to generate the data we use to generate the final configs
def cleanupfilesmenu():
    answer=True
    while answer:
        answer=input("Clean up config files Y/N?")
        if answer=="Y":
            os.remove("interface_configs.txt")
            os.remove("SQL_CSV_Export.csv")
            return

        elif answer=="N":
            return

        else:
            print("\n Invalid choice")


# Call of SQL to CSV function
sqltocsv()
# Specify source CSV data
source_csv_file = "SQL_CSV_Export.csv"
# Specify jinja template file
interface_template_file = "switchport-interface-template.j2"

# Cisco NXOS sandbox login info
device = {
             "address": "sbx-nxos-mgmt.cisco.com",
             "device_type": "cisco_nxos",
             "ssh_port": 8181,
             "username": "admin",
             "password": "Admin_1234!"
            }


# var that will contain all the final config that will be send to the switch
interface_configs = ""

# Open up the Jinja template file (as text) and then create a Jinja Template Object
with open(interface_template_file) as f:
    interface_template = Template(f.read(), keep_trailing_newline=True)

# Open the SQL generated CSV file containing the config data, we wan't to send to the device
with open(source_csv_file) as f:
    # CSV DictReader to get data from the SQL generated CSV
    reader = csv.DictReader(f)
    # For each row in the SQL generated CSV, generate an interface config by using the jinja2 template file
    for row in reader:
        interface_config = interface_template.render(
            interface = row["Interface"],
            vlan = row["VLAN"],
            server = row["Host"],
            link = row["Host_Link"],
            purpose = row["Host_Role"]
        )

        # Merge the individual interface configs to a complete config containing all interfaces
        interface_configs += interface_config

# Saving the final configuraiton to a .txt file
with open("interface_configs.txt", "w") as f:
    f.write(interface_configs)

# Connection handler from netmiko to connect and send config to the device
with ConnectHandler(ip = device["address"],
                    port = device["ssh_port"],
                    username = device["username"],
                    password = device["password"],
                    device_type = device["device_type"]) as ch:

    config_set = interface_configs.split("\n")
    output = ch.send_config_set(config_set)
    print(output)

cleanupfilesmenu()
