from socket import socket, AF_INET, SOCK_STREAM, SHUT_RDWR
from time import sleep

SERVER_ADDRESS = ('localhost', 6330)
BUFF_SIZE = 512
ENCODING = 'utf-8'


def print_mess(text):
    print('(Client): {}'.format(text))


def print_dotted(value):
    print('\n' + '-' * 16 + '{}'.format(value) + '-' * 16)


def chat_client():
    print_dotted('CHAT CLIENT')
    try:
        client_socket = socket(AF_INET, SOCK_STREAM)
        print_mess('Socket created')

        try:
            client_socket.connect(SERVER_ADDRESS)
            print_mess('Connected successfully to => {}'.format(SERVER_ADDRESS[0]))
            sleep(2)
            while True:
                input_msg = input('Enter message: ')
                try:
                    client_socket.sendall(input_msg.encode(ENCODING))
                    print_mess('Sent => {}'.format(input_msg))
                    if '[STOP]' in input_msg:
                        break
                    data = client_socket.recv(BUFF_SIZE)
                    str_data = data.decode(ENCODING)
                    res_msg = '(SERVER) => {}'.format(str_data)
                    print(res_msg)
                except Exception as e:
                    print_mess(e)
        except Exception as e:
            print_mess(e)
        finally:
            client_socket.close()
            print_dotted('CONNECTION HAS ENDED')

    except Exception as e:
        print_mess(e)


chat_client()
