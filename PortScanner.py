import socket
from IPy import IP

start = int(input("Enter the port you want your scan to start with: "))
end = int(input("Enter the port you want your scan to end with: "))

def multiple_scan(ipaddress):
    convertedIP = check_ip(ipaddress)
    print("\n" + "Scanning Target: " + str(ipaddress))
    # Specifying a range of ports to scan
    for port in range(start, end + 1):
        port_scan(convertedIP, port)

# Make the domain name of a web page to be accepted
def check_ip(ip):
    try:
        IP(ip)
        return (ip)
    except ValueError:
        return socket.gethostbyname(ip)

timer = float(input("Enter the timer you want your scan to take for each port in seconds (the bigger the better resutls): "))

# Scanning ONE port based on an IP address
def port_scan(ipaddress, port):
    try:
        socketObject = socket.socket()
        # Set the time for each port to be scanned
        socketObject.settimeout(timer)
        # Connect to the port
        socketObject.connect((ipaddress, port))
        print("The port " + str(port) + " is open!")
    except:
        pass



ipaddress = input("Enter the IP you want to scan, to scan more than one target split them with the '+' symbol: ")

if '+' in ipaddress:
    for ip in ipaddress.split('+'):
        multiple_scan(ip.strip(' '))
else:
    multiple_scan(ipaddress)
