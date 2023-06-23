import socket
from json import loads
from InquirerPy import prompt
from os import path, makedirs
from InquirerPy.base import Choice
from utils import send_msg, download
from InquirerPy.utils import patched_print, color_print


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
                    Choice(value='ed', name="Exit & Disconnect")
                ],
                "default": 'c',
            }
        ]
        answers = prompt(main_questions)
        return answers

    main_answer = main()
    con_questions = [
        {"type": "input", "message": "Enter Server Host:"},
        {"type": "input", "message": "Enter Server port:"},
    ]


    match main_answer[0]:
        case 'c':
            con_answers = prompt(con_questions)
            connect(con_answers[0], int(con_answers[1]))
            cli()

        case 'l':
            ld = dir_ls()
            for i in ld:
                color_print([("green", f'\t 📄 {i}')])
            cli()
        
        case 'd':
            ld = dir_ls()
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
            if download(sc, path):
                patched_print(f'\t{path} Received successfully!')
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


def dir_ls():
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