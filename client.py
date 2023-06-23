import socket
from json import loads
from InquirerPy import prompt
from os import path, makedirs
from InquirerPy.base import Choice
from InquirerPy.utils import patched_print, color_print
from utils import send_msg, download_file, upload_file, dir_ls


def cli():
    def main():
        main_questions = [
            {
                "type": "list",
                "message": "What can I do my Lord?",
                "choices": [
                    Choice(value='c', name="Connect"),
                    Choice(value='l', name="List"),
                    Choice(value='d', name="Download"),
                    Choice(value='u', name="Upload"),
                    Choice(value='ed', name="Exit & Disconnect")
                ],
                "default": 'c',
            }
        ]
        answers = prompt(main_questions)
        return answers

    main_answer = main()

    match main_answer[0]:
        case 'c':
            con_questions = [
                {"type": "input", "message": "Enter Server Host:"},
                {"type": "input", "message": "Enter Server port:"},
            ]
            con_answers = prompt(con_questions)
            connect(con_answers[0], int(con_answers[1]))
            cli()

        case 'l':
            ld = get_dir_ls()
            for i in ld:
                color_print([("green", f'\t 📄 {i}')])
            cli()
        
        case 'd':
            ld = get_dir_ls()
            d_question = [{
                "type": "rawlist",
                "choices": ld,
                "message": "Select file to download:",
                "multiselect": False,
                "validate": lambda result: len(result) > 0,
                "invalid_message": "Select a file"
            }]
            d_answers = prompt(d_question)
            send_msg(sc, {'msg': 'd', 'name': d_answers[0]})
            path = f'{dir}/{d_answers[0]}'
            if download_file(sc, path):
                patched_print(f'\t{path} Received successfully!')
            cli()

        case 'u':
            ld = dir_ls(dir)
            u_question = [{
                "type": "rawlist",
                "choices": ld,
                "message": "Select file to upload:",
                "multiselect": False,
                "validate": lambda result: len(result) > 0,
                "invalid_message": "Select a file"
            }]
            u_answers = prompt(u_question)
            send_msg(sc, {'msg': 'u', 'name': u_answers[0]})
            path = f'{dir}/{u_answers[0]}'
            if upload_file(sc, path):
                patched_print(f'\t{path} Uploaded successfully!')
            cli()

        case 'ed':
            disconnect()


def connect(host, port):
    try:
        sc.connect((host, port))  # connect to the server
        patched_print('Connected')
    except Exception as e:
        patched_print(e)


def disconnect():
    try:
        send_msg(sc, {'msg': 'ed'})
        sc.close()
        patched_print('Disconnected')
    except Exception as e:
        patched_print(e)


def get_dir_ls():
    try:
        send_msg(sc, {'msg': 'list'})
        data = sc.recv(bs).decode()  # receive response
        return loads(data).get('list')
    except Exception as e:
        patched_print(e)


if __name__ == '__main__':
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bs = 4096
    dir = 'horizon'

    if not path.exists(dir):
        makedirs(dir)

    connect('N55', 5000) # test connection
    cli()