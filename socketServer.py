import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
print(ADDR)
FORMAT = "UTF-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def disconnect(msg):
	print("[CLIENT] DISCONNECTING")


def message_handler(msg):
	pass


def submit_name(msg):
	data = msg.split()
	name = data[1]
	color = data[2]
	print(f"[ADDING PLAYER] added {name} with color {color}")


def submit_move(msg):
	data = msg.split()
	color = data[1]
	pawn = data[2]
	print(f"[SERVER] capturing {pawn} from {color}")


PARSING_LIST = {
	DISCONNECT_MESSAGE: "DISCONNECTING USER",
	"SUBMIT_PLAYER": "SUBMITTING NAME",
	"SUBMIT_MOVE": "SUBMITTING MOVE"
}

FUNCTION_LIST = {
	DISCONNECT_MESSAGE: disconnect,
	"SUBMIT_PLAYER": submit_name,
	"SUBMIT_MOVE": submit_move
}


def handle_client(conn, addr):
	print(f"[NEW CONNECTION] {addr} connected.\n")

	connected = True
	while connected:
		# receiving the message
		msg_length = conn.recv(HEADER).decode(FORMAT)
		if msg_length:
			msg_length = int(msg_length)
			msg = conn.recv(msg_length).decode(FORMAT)
			if msg == DISCONNECT_MESSAGE:
				connected = False
			print(f"[CLIENT] {addr[0]} {msg}")
			conn.send("Msg received".encode(FORMAT))
			
			# handling the message
			data = msg.split()
			dataKey = data[0]
			
			try:
				action = PARSING_LIST[dataKey]
				print(f"[SERVER] {action}")
				FUNCTION_LIST[dataKey](msg)
			except KeyError:
				print(f"[SERVER] UNKNOWN REQUEST")
				
	conn.close()


def start():
	server.listen()
	print("[SERVER] server now listening")
	while True:
		conn, addr = server.accept()
		thread = threading.Thread(target=handle_client, args=(conn, addr))
		thread.start()
		print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[starting server] starting listener")
start()