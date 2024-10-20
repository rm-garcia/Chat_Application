import socket
import threading

HOST = '127.0.0.1'
PORT = 56787
LISTENER_LIMIT = 10
clients = {}
usernames = {}

def handle_client(client):
    """Handle communication with a client."""
    try:
        # Get the username from the client
        username = client.recv(1024).decode('utf-8')
        usernames[client] = username
        welcome_message = f"{username} has joined the chat!"
        broadcast(welcome_message)
        print(welcome_message)

        while True:
            # Receive message from client
            message = client.recv(1024).decode('utf-8')
            broadcast(message, username)
    except:
        # Handle client disconnection
        remove_client(client)

def broadcast(message, sender_username=""):
    """Send a message to all connected clients except the sender."""
    for client in clients:
        try:
            if usernames[client] != sender_username:  # Do not send the message back to the sender.
                client.send(message.encode('utf-8'))
        except:
            # Handle broken connections by removing the client
            remove_client(client)

def remove_client(client):
    """Remove a client from the list and close its connection."""
    if client in clients:
        client_address = clients[client]
        client_username = usernames.get(client, "Unknown")
        del clients[client]
        del usernames[client]
        client.close()
        left_message = f"{client_username} has left the chat."
        broadcast(left_message)
        print(left_message)

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((HOST, PORT))
        print(f"Server running on {HOST} {PORT}")
    except:
        print(f"Couldn't bind to host {HOST} port {PORT}")
        return

    server.listen(LISTENER_LIMIT)
    print(f"Listening for connections...")

    while True:
        client, address = server.accept()
        print(f"Connection from {address} established.")
        
        clients[client] = address
        client.send("Connected to the server! ".encode('utf-8'))

        # Start a new thread to handle this client
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == '__main__':
    main()
