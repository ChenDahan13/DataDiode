import socket
import time
import hashlib


PROXY_1_IP = '127.0.0.1'
PROXY_1_PORT = 5000

filename = 'file.txt'
BUFFER_SIZE = 8192


def send_to_proxy():
    # Create connection to Proxy1
    send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    send_socket.connect((PROXY_1_IP,PROXY_1_PORT))
    print('Connect to Proxy1')

    # Sending the hash
    send_the_hash(send_socket)

    # Sending the file
    send_the_file(send_socket)

    send_socket.close()

def send_the_hash(send_socket):
    print('Start sending the hash')
    hash_md5 = hashlib.md5()

    # open the file
    with open(filename, 'rb') as file:
        for chunk in iter(lambda: file.read(BUFFER_SIZE), b""):
            hash_md5.update(chunk)

    send_socket.send(hash_md5.hexdigest().encode())
    print('Hash was sent')
    time.sleep(0.3)
    file.close()

def send_the_file(send_socket):
    print('Start sending the file')

    # open the file
    with open(filename, 'rb') as file:
        # divide file to chunks and send them
        data = file.read(BUFFER_SIZE)
        while data:
            send_socket.send(data)
            print(f'Packet was sent, length {len(data)}')
            time.sleep(0.3)
            data = file.read(BUFFER_SIZE)

    print('File was sent')
    file.close()

if __name__ == '__main__':
    send_to_proxy()
