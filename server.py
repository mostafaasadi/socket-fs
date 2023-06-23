import socket
from time import sleep
from json import loads
from utils import send_msg, send_file
from os import listdir, path, makedirs


def dir_ls():
    ld = listdir(dir)
    return ld

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
                ld = dir_ls()
                send_msg(conn, {'list': ld})
            
            case 'd':
                path = f'{dir}/{data["name"]}'
                send_file(conn, path)
            
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
