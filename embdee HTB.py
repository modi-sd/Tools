import requests
from bs4 import BeautifulSoup
import hashlib
req = requests.session()
url = "http://docker.hackthebox.eu:30114/"
r = req.get(url)
r.txt0 = BeautifulSoup(r.text, "html.parser")
r.txt1 = str(r.txt0).replace("""<html>
<head>
<title>emdee five for life</title>
</head>
<body style="background-color:powderblue;">
<h1 align="center">MD5 encrypt this string</h1><h3 align="center">""","")
r.txt2 = str(r.txt1).replace("""</h3><center><form action="" method="post">
<input align="center" name="hash" placeholder="MD5" type="text"/>
</form></center></body></html>
<input type="submit" value="Submit"/>



""","")
data = { 'hash' : hashlib.md5(r.txt2.encode('utf-8')).hexdigest()}
r1 = req.post(url, data = data)
print(r.txt2,data,r1.text)
