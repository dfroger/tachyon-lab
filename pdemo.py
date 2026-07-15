import multiprocessing
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
    procs = [
        multiprocessing.Process(target=sub_processing),
        multiprocessing.Process(target=sub_processing),
        multiprocessing.Process(target=sub_processing),
    ]
    for p in procs:
        p.start()
    for p in procs:
        p.join()


def post_processing():
    time.sleep(DELAY)


def request():
    pre_processing()
    processing()
    post_processing()


if __name__ == "__main__":
    request()
