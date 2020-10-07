import telnetlib
import getpass
import time


def connect_ssh_send_config():
    # DevNet Sandbox Nexus 9000 switch to send configuration to
    device = {
             "address": "sbx-nxos-mgmt.cisco.com",
             "device_type": "cisco_nxos",
             "ssh_port": 8181,
             "username": "admin",
             "password": "Admin_1234!"
            }
    # Use Netmiko to connect to the device and send the configuration
    with ConnectHandler(ip = device["address"],
                        port = device["ssh_port"],
                        username = device["username"],
                        password = device["password"],
                        device_type = device["device_type"]) as ch:
        config_set = interface_configs.split("\n")
        output = ch.send_config_set(config_set)
        print(output)

def connect_telnet():
    """HOST=”192.168.43.10″
    user = raw_input(“Enter your telnet username:“)
    password = getpass.getpass()
    tn = telnetlib.Telnet(HOST)

    tn.read_until(“Username: “)

    tn.write(user + “\n”)

    if password:

    tn.read_until(“Password: “)

    tn.write(password + “\n”)

    tn.write(“enable\n”)    ##changing to enable mode
    tn.write(“cisco\n”)      ##providing enable password
    tn.write(“conf t\n”)     ##moving to configuration mode
    tn.write(“int vlan 10 \n”)   ##changing to vlan 10 interface
    tn.write(“ip address 1.1.1.1 255.255.255.255\n”)  ##Assigning the IP address
    tn.write(“end\n”)    ##ending the configuration
    tn.write(“exit\n”)"""

def getserialport():
    import serial.tools.list_ports
    ports = serial.tools.list_ports.comports()

    for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))

def connect_serial():
    print()



