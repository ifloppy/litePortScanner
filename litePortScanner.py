#Made by iruanp.com
import socket,threading

def socket_connect(Host, port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(3)

    try:
        sk.connect((Host, port))
        print("Connected to port "+str(port)+" successfully!")
    except Exception:
        pass



host_=input("Please input your host:")

for i in range(65536):
    threading.Thread(target=socket_connect, args=(host_, i)).start()
