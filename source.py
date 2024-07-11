#Domain to IP
import socket
import pyfiglet
from termcolor import colored

banner = colored(pyfiglet.figlet_format('Domain To Ip'),'green')
print(banner)
domain_name = input("Enter your domain name: ")
ip = socket.gethostbyname(domain_name)
print('Ip for {} : {}'.format(domain_name,ip))
