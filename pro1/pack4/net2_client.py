# 단순 클라이언트
from socket import *

clientsock = socket(AF_INET, SOCK_STREAM)
clientsock.connect(('192.168.0.30', 7878))     # 능동적으로 server에 접속
clientsock.send('ㅋㅋㅋㅋㅋ'.encode(encoding='utf_8')) # 송신 # errors='strict' (엄격체크)
re_msg = clientsock.recv(1024).decode() # 수신
print('수신자료 : ', re_msg)
clientsock.close()

