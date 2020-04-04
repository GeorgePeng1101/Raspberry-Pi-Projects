import socket

HOST = '192.168.50.32'
PORT = 3333
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

request = '{\"id\":0,\"jsonrpc\":\"2.0\",\"method\":\"miner_getstat2\"}'
request = request.encode()
s.sendall(request)

s.shutdown(socket.SHUT_WR)
data = b''
while True:
    buf = s.recv(1024)
    if not buf:
        break
    data += buf
s.close()
print('Received', repr(data))
