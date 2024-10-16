import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog, messagebox

HOST = '127.0.0.1'
PORT = 56787

class ChatClient:
    def __init__(self, master):
        self.master = master
        self.master.title("Chat Client")
        
        self.chat_area = scrolledtext.ScrolledText(master, state='disabled', wrap='word')
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.message_entry = tk.Entry(master)
        self.message_entry.pack(padx=10, pady=10, fill=tk.X)
        self.message_entry.bind("<Return>", self.send_message)

        self.username = None
        self.client = None

        self.connect_to_server()

    def connect_to_server(self):
        """Connect to the server and get the username."""
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client.connect((HOST, PORT))
            print("Connection Successful.")
            self.username = self.get_username()
            self.client.send(self.username.encode('utf-8'))

            # Start a thread to receive messages
            receive_thread = threading.Thread(target=self.receive_messages)
            receive_thread.start()
        except Exception as e:
            messagebox.showerror("Connection Error", f"Could not connect to the server: {e}")

    def get_username(self):
        """Prompt for a username and return it."""
        username = simpledialog.askstring("Username", "Enter your username:")
        if username:
            return username
        else:
            messagebox.showerror("Username Error", "Username cannot be empty.")
            self.master.quit()

    def receive_messages(self):
        """Receive messages from the server and display them."""
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                self.chat_area.config(state='normal')
                self.chat_area.insert(tk.END, message + '\n')
                self.chat_area.config(state='disabled')
                self.chat_area.yview(tk.END)  # Auto-scroll to the end
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
                self.client.close()
                break

    def send_message(self, event=None):
        """Send a message to the server and display it in the chat area."""
        message = self.message_entry.get()
        if message:
            full_message = f"{self.username}: {message}"
            
            # Display the sent message in the chat area
            self.chat_area.config(state='normal')
            self.chat_area.insert(tk.END, full_message + '\n')
            self.chat_area.config(state='disabled')
            self.chat_area.yview(tk.END)  # Auto-scroll to the end
            
            # Send the message to the server
            self.client.send(full_message.encode('utf-8'))
            self.message_entry.delete(0, tk.END)  # Clear the entry box

if __name__ == '__main__':
    root = tk.Tk()
    chat_client = ChatClient(root)
    root.mainloop()