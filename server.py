import socket
from os import listdir
from json import dumps
from time import sleep


def dir_ls():
    ld = listdir(dir)
    return ld


def send_msg(conn, msg):
    try:
        conn.send(dumps(msg).encode())
    except Exception as e:
        print(e)


def server_program():
    conn, address = ss.accept()  # accept new connection
    print("Connection from: " + str(address))
    data = None
    while True:
        sleep(st) # cpu usage
        data = conn.recv(bs).decode()
        match data:
            case 'list':
                ld = dir_ls()
                send_msg(conn, {'list': ld})
            case 'd':
                conn.close()
                break


if __name__ == '__main__':
    # Configs
    port = 5000
    bs = 2048 # buffer size
    dir = 'blackhole' # directory
    st = 0.001 # sleep time

    # get the hostname
    host = socket.gethostname()
    print(f'server on {host}:{port} is running ...')
    ss = socket.socket()  # get instance
    ss.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    ss.listen(2)
    server_program()
