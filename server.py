import socket
from time import sleep
from json import loads
from os import path, makedirs
from utils import send_msg, upload_file, dir_ls, download_file


def server_program():
    conn, address = ss.accept()  # accept new connection
    print("Connection from: " + str(address))
    data = None
    while True:
        sleep(st) # cpu usage
        de = conn.recv(bs).decode()
        if not de:
            continue
        data = loads(de)

        match data['msg']:
            case 'list':
                ld = dir_ls(dir)
                send_msg(conn, {'list': ld})
            
            case 'd':
                path = f'{dir}/{data["name"]}'
                if upload_file(conn, path):
                    print(f'\t{path} sended successfully!')

            case 'u':
                path = f'{dir}/{data["name"]}'
                if download_file(conn, path):
                    print(f'\t{path} Recieved successfully!')
            
            case 'ed':
                conn.close()
                break


if __name__ == '__main__':
    # Configs
    port = 5000
    bs = 4096 # buffer size
    dir = 'blackhole' # directory
    st = 0.001 # sleep time

    # get the hostname
    host = socket.gethostname()
    if not path.exists(dir):
        makedirs(dir)
    ss = socket.socket()  # get instance
    ss.bind((host, port))  # bind host address and port together
    print(f'server on {host}:{port} is running ...')

    # configure how many client the server can listen simultaneously
    ss.listen(2)
    server_program()
