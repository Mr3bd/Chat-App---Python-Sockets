from socket import socket, AF_INET, SOCK_STREAM, SHUT_RDWR

SERVER_ADDRESS = ('localhost', 6330)
BUFF_SIZE = 512
ENCODING = 'utf-8'


def print_mess(text):
    print('(Server): {}'.format(text))


def print_dotted(value):
    print('\n' + '-' * 16 + '{}'.format(value) + '-' * 16)


def chat_server():
    print_dotted('CHAT SERVER')
    print_mess('Start at: {}'.format(SERVER_ADDRESS))

    try:
        server_sock = socket(AF_INET, SOCK_STREAM)
        print_mess('Socket created')
        print_mess('[IP] => {}'.format(SERVER_ADDRESS[0]))
        print_mess('[PORT] => {}'.format(SERVER_ADDRESS[1]))

        try:
            server_sock.bind(SERVER_ADDRESS)
            print_mess('Binding success')

            server_sock.listen()
            print_mess('Listening...')

            try:
                conn, add = server_sock.accept()
                print_mess('Accepted connection ({})'.format(add))
                while True:
                    data = conn.recv(BUFF_SIZE)
                    str_data = data.decode(ENCODING)
                    res_msg = '(CLIENT) => {}'.format(str_data)
                    print(res_msg)

                    if '[STOP]' in str_data:
                        conn.sendall('STOPPED, BYE!'.encode(ENCODING))
                        conn.close()
                        break
                    else:
                        input_msg = input('Enter message: ')
                        conn.sendall(input_msg.encode(ENCODING))
                        print_mess('Sent => {}'.format(input_msg))
            except Exception as e:
                print_mess(e)

        except Exception as e:
            print_mess(e)
        finally:
            server_sock.close()
            print_dotted('CONNECTION HAS ENDED')

    except Exception as e:
        print_mess(e)


chat_server()
