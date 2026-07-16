import threading
import time

DELAY = 0.5

def pre_processing():
    time.sleep(DELAY)


def foo():
    time.sleep(DELAY)


def bar():
    time.sleep(DELAY)


def baz():
    time.sleep(DELAY)


def sub_processing():
    foo()
    bar()
    baz()


def processing():
    threads = [
        threading.Thread(target=sub_processing),
        threading.Thread(target=sub_processing),
        threading.Thread(target=sub_processing),
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def post_processing():
    time.sleep(DELAY)


def request():
    pre_processing()
    processing()
    post_processing()


request()
