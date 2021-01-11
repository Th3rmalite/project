import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.192.47"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

def send_capture(color,pawnIdx):
	msg = f"SUBMIT_MOVE {color} {pawnIdx}"
	send(msg)

if __name__ == "__main__":
	send("SUBMIT_PLAYER Vincent red")
	send_capture("red", 4)
	input()
	send(DISCONNECT_MESSAGE)