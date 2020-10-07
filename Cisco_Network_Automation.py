import os
from jinja2 import Template
from netmiko import ConnectHandler
from SQL_Connection import *
from Connection_Functions import *


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


sqltocsv()
source_csv_file = "SQL_CSV_Export.csv"
interface_template_file = "switchport-interface-template.j2"

# DevNet Sandbox Nexus 9000 switch to send configuration to
device = {
             "address": "sbx-nxos-mgmt.cisco.com",
             "device_type": "cisco_nxos",
             "ssh_port": 8181,
             "username": "admin",
             "password": "Admin_1234!"
            }


# String that will hold final full configuration of all interfaces
interface_configs = ""

# Open up the Jinja template file (as text) and then create a Jinja Template Object
with open(interface_template_file) as f:
    interface_template = Template(f.read(), keep_trailing_newline=True)

# Open up the CSV file containing the data
with open(source_csv_file) as f:
    # Use DictReader to access data from CSV
    reader = csv.DictReader(f)
    # For each row in the CSV, generate an interface configuration using the jinja template
    for row in reader:
        interface_config = interface_template.render(
            interface = row["Interface"],
            vlan = row["VLAN"],
            server = row["Host"],
            link = row["Host_Link"],
            purpose = row["Host_Role"]
        )

        # Append this interface configuration to the full configuration
        interface_configs += interface_config

# Save the final configuraiton to a file
with open("interface_configs.txt", "w") as f:
    f.write(interface_configs)

# Use Netmiko to connect to the device and send the configuration
with ConnectHandler(ip = device["address"],
                    port = device["ssh_port"],
                    username = device["username"],
                    password = device["password"],
                    device_type = device["device_type"]) as ch:

    config_set = interface_configs.split("\n")
    output = ch.send_config_set(config_set)
    print(output)

cleanupfilesmenu()
