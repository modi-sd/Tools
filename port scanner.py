import socket # for connecting
from colorama import init, Fore
import pyfiglet
ascii_banner = pyfiglet.figlet_format("MAWSO3A89")
print(ascii_banner)
def main():
    # some colors
    init()
    green = Fore.GREEN
    reset =Fore.RESET
    gray = Fore.LIGHTBLACK_EX
    host = input("Enter Host To Scan:")
    def is_port_open(host, port):
        #creates a new socket
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            s.connect((host, port))
            s.settimeout(0.2)
        except:
            #cannot connect, port is closed
            #return false
            return False
        else:
            return True
    scantype = input("1 for port range \n2 for scan one port\nEnter Scan Type:")
    if scantype == "2" :
         port = int(input("Enter Port Nnumber:"))
         if is_port_open(host, port):
             print(f"{green}[+] {host}:{port} is open {reset} \n")
         else:
                 print(f"{gray}[-] {host}:{port} is closed {reset} \n")
    elif scantype == "1":
             ports = int(input("Enter First port"))
             porte = input("Enter Last Port:")
             porte = int(porte) + int(1)
             for port in range(ports,porte):
                 if is_port_open(host, port):
                     print(f"{green}[+] {host}:{port} is open {reset} \n")
                 else:
                     print(f"{gray}[-] {host}:{port} is closed {reset} \n")
    else:
                     print("choose from the fookin scantype")
                     main()
main()

    
    
    


