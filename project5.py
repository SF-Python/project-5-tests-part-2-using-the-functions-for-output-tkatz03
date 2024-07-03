'''
Github Handle: tkatz03
Course: COP2002 0M1
Created: July 2, 2024
Program Title: Project 5 
Description: This program is an interactive study tool that helps users prepare for the CompTIA A+ certification by quizzing them on matching port numbers with their corresponding protocols.
'''

import random

# Port numbers and corresponding protocols as parallel arrays
ports = ["20", "21", "22", "23", "25", "53", "67", "68", "80", "110", "137", "139", "143", "161", "162", "389", "443", "445", "3389"]
protocols = ["FTP", "FTP", "SSH", "Telnet", "SMTP", "DNS", "DHCP", "DHCP", "HTTP", "POP3", "NetBIOS", "NetBIOS", "IMAP", "SNMP", "SNMP", "LDAP", "HTTPS", "SMB", "RDP"]

# Finds the protocol name based on the port number chosen
def numToName(portNumArray, portNameArray, portNumber):
    for i in range(len(portNumArray)):
        if portNumArray[i] == portNumber:
            return portNameArray[i]
    return None
    
# Finds the port number based on the protocol name chosen
def nameToNum(portNumArray, portNameArray, portName):
    result = []
    for i in range(len(portNameArray)):
        if portNameArray[i] == portName:
            result.append(portNumArray[i])
    return result

# Gets input from the user and checks if it is valid
def getInput():
    while True:
        choice = input("Choice: ").strip()
        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Displays the main menu text
def display_main_menu():
    print("Main Menu:")
    print("1. Given a port number, identify the PROTOCOL (use abbreviation).")
    print("2. Given a port protocol, identify a port NUMBER.")
    print("3. Exit\n")

# Option 1: Identify the port's protocol
def option_1():
    print("Option 1: Identify the port's PROTOCOL.")
    print("----------------------------------------\n")
    while True:
        port = random.choice(ports)
        answer = input(f"What is the protocol for port {port} (m=Main Menu)? ").strip()
        if answer.lower() == 'm':
            print()  
            break
        correct_protocol = numToName(ports, protocols, port)
        if answer == correct_protocol:
            print("Correct answer!\n")
        else:
            print(f"Incorrect. The correct answer is {correct_protocol}.\n")

# Option 2: Identify the port's number
def option_2():
    print("Option 2: Identify the port's NUMBER.")
    print("----------------------------------------\n")
    while True:
        protocol = random.choice(protocols)
        answer = input(f"What is the number for protocol {protocol} (m=Main Menu)? ").strip()
        if answer.lower() == 'm':
            print() 
            break
        correct_ports = nameToNum(ports, protocols, protocol)
        if answer in correct_ports:
            print("Correct answer!\n")
        else:
            print(f"Incorrect. The correct answer is {', '.join(correct_ports)}.\n")

# Main program loop
def main():
    while True:
        display_main_menu()
        choice = getInput()
        if choice == '1':
            option_1()
        elif choice == '2':
            option_2()
        elif choice == '3':
            print("\nProgram Complete. I hope this has helped in studying for the CompTIA A+ certification.")
            break

if __name__ == "__main__":
    main()
