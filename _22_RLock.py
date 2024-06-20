import threading

class Unit(threading.Thread):
    def __init__(self):
        super().__init__()
        self.var = 10
        self.lock = threading.RLock()

    def Foo(self):
        with self.lock:
            self.var += 1
            self.Bar()

    def Bar(self):
        with self.lock:
            self.var += 1

    def Baz(self):
        with self.lock:
            self.var += 1

    def run(self):
        self.Foo()
        self.Bar()
        self.Baz


t1 = Unit()
t1.start()

t2 = Unit()
t2.start()