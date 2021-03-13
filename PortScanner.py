import socket
from IPy import IP

starting_port = int(input("Enter the port you want your scan to start with: "))
ending_port = int(input("Enter the port you want your scan to end with: "))


# Make able multiple scans to be done
def multiple_scan(ip_address):
    convertedIP = check_ip(ip_address)
    print("\n" + "Scanning Target: " + str(ip_address))
    # Specifying a range of ports to scan
    for port in range(starting_port, ending_port + 1):
        port_scan(convertedIP, port)


# Make the domain name of a web page to be accepted
def check_ip(ip):
    try:
        IP(ip)
        return (ip)
    except ValueError:
        return socket.gethostbyname(ip)


# Get the time for each scan
timer = float(
    input("Enter the timer you want your scan to take for each port in seconds (the bigger the better results): "))


# Scanning one port based on an IP address
def port_scan(ip_address, port):
    try:
        socketObject = socket.socket()
        # Set the time for each port to be scanned
        socketObject.settimeout(timer)
        # Connect to the port
        socketObject.connect((ip_address, port))
        print("The port " + str(port) + " is open!")
    except:
        pass


ip_address = input("Enter the IP you want to scan, to scan more than one target split them with the '+' symbol: ")

# Separate each ip address or domain name with the + symbol
if '+' in ip_address:
    for ip in ip_address.split('+'):
        multiple_scan(ip.strip(' '))
else:
    multiple_scan(ip_address)
