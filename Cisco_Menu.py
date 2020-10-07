import os
from datetime import datetime
from SQL_Connection import *


def main_menu():
    answer=True
    while answer:
        print("""
        1.Configuration menu
        2.List switch settings from database
        3.Automation Log
        4.Quit
        """)
        answer=input("Which menu will you like to open?")
        if answer=="1":
            config_menu()

        elif answer=="2":
            printsqlswitchconfig()

        elif answer=="3":
            automation_log_menu()

        elif answer=="4":
            print("Bye")
            answer = None

        else:
           print("\n Invalid choice")


def config_menu():
    answer=True
    while answer:
        print("""
        1a.Run Auto config with SSH
        1b.TELNET
        1c.CONSOLE CONNECTION
        1d.Exit to main menu
        """)
        answer=input("How would you like to connect to the network equipment?")
        if answer=="1a":
            exec(open("Cisco_Network_Automation.py").read())
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            switch_name = "sbx-n9kv-ao"
            config_type = "Automated"
            InsertLog(timestamp, switch_name, config_type)

        elif answer=="1b":
            print("Feature not ready yet")

        elif answer=="1c":
            print("Feature not ready yet")

        elif answer=="1d":
            main_menu()

        else:
            print("\n Invalid choice")


def automation_log_menu():
    answer=True
    while answer:
        print("""
        3a.Print Config_Log
        3b.Clear first 10 log entries
        3c.Clear logs
        3d.Exit to main menu
        """)
        answer=input("What would you like to do?")
        if answer=="3a":
            printsqlconfiglog()

        elif answer=="3b":
            clearfirst10log_entries()

        elif answer=="3c":
            clearlog()

        elif answer=="3d":
            main_menu()

        else:
            print("\n Invalid choice")


main_menu()
