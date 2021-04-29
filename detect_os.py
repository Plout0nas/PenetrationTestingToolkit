from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr1

# if this runs on windows 10 you need to have npcap installed (https://nmap.org/npcap/)
# change this to whatever you want
DST_IP = '192.168.1.19'


def passive(dst):
	"""
		+------------------+
		|   OS TTL Values  |
		+---------+--------+
		| OS      | IP TTL |
		+---------+--------+
		| Linux   |     64 |
		+---------+--------+
		| Windows |    128 |
		+---------+--------+
		|         |        |
		+---------+--------+
		|         |        |
		+---------+--------+
	"""
	
	ip_packet = IP(dst=dst)/ICMP()
	packet_resp = sr1(ip_packet, timeout=4)
	
	if packet_resp is None:
		print('[!] Request timeout')
		return 'timeout'
	
	resp_ttl = packet_resp.getlayer(IP).ttl
	if resp_ttl <= 64:
		print(f'[+] Remote OS is Linux - TTL {resp_ttl}')
		return 'linux'
	elif resp_ttl <= 128:
		print(f'[+] Remote OS is Windows - TTL {resp_ttl}')
		return 'windows'
	else:
		print(f'[+] Remote OS is other or protected - TTL {resp_ttl}')
		return 'other'
	
	
if __name__ == '__main__':
	passive(DST_IP)
