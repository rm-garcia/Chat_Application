import socket
import threading

HOST = '127.0.0.1'
PORT = 56787

def receive_messages(client):
    """Receive messages from the server."""
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            # If there's an error, close the connection
            print("An error occurred. Connection closed.")
            client.close()
            break

def send_messages(client, username):
    """Send messages to the server."""
    while True:
        message = input("")
        full_message = f"{username}: {message}"
        client.send(full_message.encode('utf-8'))

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, PORT))
        print("Connection Successful.")
    except:
        print(f"Connection not made. Host: {HOST} Port: {PORT}")
        return

    # Ask for the user's username
    username = input("Enter your username: ")
    client.send(username.encode('utf-8'))

    # Start a thread to receive messages
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    # Start a thread to send messages
    send_thread = threading.Thread(target=send_messages, args=(client, username))
    send_thread.start()

if __name__ == '__main__':
    main()
