import nmap

nm = nmap.PortScanner()

# vale to ip pou thes na testareis

machine = nm.scan('127.0.0.1', arguments='-O')

print(machine['scan']['127.0.0.1']['osmatch'][0]['osclass'][0]['osfamily'])
