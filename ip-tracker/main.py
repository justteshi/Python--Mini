import socket
hostname = socket.gethostname()
ip_adress = socket.gethostbyname(hostname)

print('Your Pc\'s name is:' + hostname)
print('Your IP Adress is:' + ip_adress)
