import socket
import threading
from urllib.request import urlopen
import queue
import re
import operator
import json
import itertools
from argparse import ArgumentParser


def calculate_statistict(text, top_k_words):
    words = re.findall("[\w-]+", text)
    word_frequancy = {}
    for word in words:
        if word in word_frequancy.keys():
            word_frequancy[word] += 1
        else:
            word_frequancy[word] = 1
    
    word_frequancy = dict(sorted(word_frequancy.items(), key=operator.itemgetter(1)))
    word_frequancy = dict(itertools.islice(word_frequancy.items(), top_k_words))
    # return json.dumps(word_frequancy)
    return str(word_frequancy)


# def get_text_url(que):
#     resp = urlopen(que.get(timeout=1))
#     word_frequancy = calculate_statistict(resp.read().decode("utf-8"), top_k_words)
#     print(word_frequancy)


def fetch_url(sem, que, conn, top_k_words):
    while True:
        try:
            url = que.get(timeout=1)
        except queue.Empty:
            continue

        if url is None:
            print("THREAD ENDS")
            que.put(None)
            break

        with sem:
            resp = urlopen(url)
            word_frequancy = calculate_statistict(resp.read().decode("utf-8"), top_k_words)
            conn.send(word_frequancy.encode('utf-8'))


def inicialize_workers(cnt_theads, path_to_urls, conn, top_k_words):
    sem = threading.Semaphore(30)
    que = queue.Queue(maxsize=50)

    fetch_url_args = (sem, que, conn, top_k_words)
    threads = [
        threading.Thread(target=fetch_url, args=fetch_url_args) for _ in range(cnt_theads)
    ]

    with open(path_to_urls) as f:
        lines = f.readlines()
        for url in lines:
            que.put(url)
    que.put(None)

    for th in threads:
        th.start()

    for th in threads:
        th.join()


def inicialize_socket(top_k_words, cnt_theads):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("", 2145))
        sock.listen(1)

        conn, addr = sock.accept()

        while True:
            data = conn.recv(1024)
            if not data:
                break

            # path_to_urls = data.decode("utf-8")
            path_to_urls = data

            inicialize_workers(cnt_theads, path_to_urls, conn, top_k_words)
        conn.close()


if __name__ == "__main__":
    parser = ArgumentParser()    
    parser.add_argument('-w', action="store", dest='cnt_theads', type=int, default=3)
    parser.add_argument('-k', action="store", dest='top_k_words', type=int, default=3)
    results = parser.parse_args()
    cnt_theads = results.cnt_theads
    top_k_words = results.top_k_words

    if top_k_words <= 0:
        raise ValueError(f'number {top_k_words} must be > 0')

    if cnt_theads <= 0:
        raise ValueError(f'number {cnt_theads} must be > 0') 
    
    inicialize_socket(top_k_words, cnt_theads)
    
    # que = queue.Queue(maxsize=50)
    # with open('url.txt') as f:
    #     lines = f.readlines()
    #     for url in lines:
    #         que.put(url)
    # que.put(None)

    # get_text_url(que)
