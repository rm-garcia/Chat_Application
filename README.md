# Chat Server

A simple multi-threaded chat server and client implemented in Python.

## Update

### GUI Client - client_tkinter.py

Have added a new client implementation using Tkinter for a graphical user interface.

### File Structure

- `server.py`: The main server file that handles client connections and message broadcasting.
- `client.py`: A command-line client for connecting to the chat server.
- `client_tkinter.py`: A GUI client built with Tkinter that allows users to connect to the chat server with an additional graphical interface.

## Features

- Multi-client support: Multiple users can connect simultaneously.
- Usernames: Each client can set a username, and messages will display the sender's name.
- Broadcast messaging: Messages sent by one user are broadcast to all other connected users.
- User notifications: Users are notified when someone joins or leaves the chat.
- Graphical user interface (GUI): A simple and user-friendly interface for the chat client.


## SS
[Screenshot of the project.](https://cdn.discordapp.com/attachments/758031911573520546/1297392950455828491/image.png?ex=6715c2d7&is=67147157&hm=06373596b29c6eed9ec371a0a761129c87d5231a2ce333877d63a8151520c250&)

## Technologies Used

- Python 3.x
- Socket Programming
- Threading
- Tkinter
