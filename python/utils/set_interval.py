import threading

def set_interval(func,time):
    func()
    e = threading.Event()
    while not e.wait(time):
        func()
