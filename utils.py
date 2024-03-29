from json import dumps, loads
from os import listdir, remove
from base64 import b64encode, b64decode


def send_msg(conn, msg):
    try:
        conn.send(dumps(msg).encode())
    except Exception as e:
        print(e)


def dir_ls(path):
    try:
        ld = listdir(path)
        if len(ld) == 0:
            return ['Empty Directory']
        return ld
    except Exception as e:
        print(e)
        return ['Error on file system']


def del_file(path):
    try:
        remove(path)
        return True
    except Exception as e:
        print(e)
        return False


def upload_file(conn, path):
    try:
        with open(path, 'rb') as f:
            d = f.read()
            encoded_content = b64encode(d).decode('utf-8')
            msg = {
                'msg': 'd',
                'name': path.split('/')[-1],
                'data': encoded_content
            }
            smsg = dumps(msg).encode('utf-8')
            conn.sendall(len(smsg).to_bytes(4, byteorder='big'))
            conn.sendall(smsg)
        return True
    except Exception as e:
        print(e)
        return False


def download_file(con, path):
    try:
        data_size = int.from_bytes(con.recv(4), byteorder='big') # get size in first 4 bytes

        data = b''
        while len(data) < data_size:
            packet = con.recv(min(data_size - len(data), 1024))
            if not packet:
                break
            data += packet
        if len(data) != data_size:
            print(f"Expected {data_size} bytes but received {len(data)} bytes")
            return False

        # Decode data from Base64 and save to file
        decoded_data = loads(data.decode())
        with open(f'{path}', 'wb') as fo:
            try:
                fc = b64decode(decoded_data['data'])
                fo.write(fc)
            except Exception as e:
                print(e)
        return True
    except Exception as e:
        print(e)
        return False
