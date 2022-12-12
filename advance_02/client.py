import socket
from argparse import ArgumentParser
from os.path import exists
import threading


# клиент почему-то закрывает соединение после получения первого ответа
# разбираюсь, как это исправить

def inicialize_socket(path_to_urls, sem):
    with sem:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(('localhost', 2145))
            sock.send(path_to_urls.encode('utf-8'))
            data = sock.recv(1024).decode('utf-8')
            sock.close()
        print('CLIENT')
        print(data)


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument(action="store", dest='cnt_threads', type=int, default=3)
    parser.add_argument(action="store", dest='path_to_urls', type=str, default='url.txt')
    args = parser.parse_args()    
    return args.cnt_threads, args.path_to_urls


def check_positive_int(num):
    if not isinstance(num, int):
        raise TypeError(f'number {num} must be integer')

    if num <= 0:
        raise ValueError(f'number {num} must be > 0')


def check_path(path_to_file):
    if not exists(path_to_file):
        raise FileExistsError(f'file {path_to_file} dont exists')


def inicialize_thread(cnt_theads, path_to_urls):
    sem = threading.Semaphore(30)
    
    threads = [
        threading.Thread(target=inicialize_socket, args=(path_to_urls, sem)) for _ in range(cnt_theads)
    ]

    for th in threads:
        th.start()

    for th in threads:
        th.join()


if __name__ == "__main__":
    cnt_theads, path_to_urls = parse_arguments()
    
    check_positive_int(cnt_theads)
    check_path(path_to_urls)
    inicialize_thread(cnt_theads, path_to_urls)