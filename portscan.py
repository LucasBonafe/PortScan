import socket
import sys
#coding=utf-8
try:
    host = sys.argv[1]
except:
    print('informe o host alvo\nEx.: {0} 8.8.8.8'.format(sys.argv[0]))
    exit(1)
    
ports=[21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3306, 3389, 8080]
for port in ports:
    client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.03)
    r = client.connect_ex((host, port))
    if r == 0:
        print(str(port)+(" ◄ Open"))
    else:
        print(str(port)+(" • Closed"))
print("Scan accomplished\n")
