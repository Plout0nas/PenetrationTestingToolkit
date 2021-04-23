# Python Program to Get IP Address
import socket

# Get the domain name and print its ip address
domain_name = input('Enter the domain name: ')


def multiple_domain_names(domain_name):
    print(socket.gethostbyname(domain_name))


if '+' in domain_name:
    for ip in domain_name.split('+'):
        multiple_domain_names(ip.strip(' '))
else:
    multiple_domain_names(domain_name)
