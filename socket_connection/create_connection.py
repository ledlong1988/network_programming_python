import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'www.microsoft.com'
    port = 80
    result = s.connect_ex((host, port))
    print(result)
    print('It works!')


if __name__ == '__main__':
    main()
