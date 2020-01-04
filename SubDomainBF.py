import requests
import pyfiglet
ascii_banner = pyfiglet.figlet_format("MAWSO3A89")
print(ascii_banner)
#the domain to scan
domain = input("Insert Domain To Scan:")
#read all subdomains
x = input("dictionary Dir:")
if x == "" :
    url = f"http://{domain}"
    r = requests.get(url)
    print(r)
else:
    print("Discovered SubDomains")
    file = open(x)
    #read all content
    content = file.read()
    #split by new lines
    subdomains = content.splitlines()
    for subdomain in subdomains:
         # construct the url
         url = f"http://{domain}.{subdomain}"
         r = requests.get(url)
         print(url,":", r)
         
