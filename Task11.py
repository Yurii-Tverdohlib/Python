from contextlib import contextmanager
import threading


class RWLock:
    def __init__(self):
        self.read_requests = 0
        self.readers = threading.Lock()
        self.writers = threading.Lock()

    def r_lock(self):
        self.readers.acquire()
        self.read_requests += 1
        if self.read_requests == 1:
            self.writers.acquire()
        self.readers.release()

    def w_lock(self):
        self.writers.acquire()

    def r_release(self):
        assert self.read_requests > 0
        self.readers.acquire()
        self.read_requests -= 1
        if self.read_requests == 0:
            self.writers.release()
        self.readers.release()

    def w_release(self):
        self.writers.release()

    @contextmanager
    def r_locked(self):
        try:
            self.r_lock()
            yield
        finally:
            self.r_release()

    @contextmanager
    def w_locked(self):
        try:
            self.w_lock()
            yield
        finally:
            self.w_release()


class Example:
    def __init__(self):
        self.rwlock = RWLock()

    def read(self):
        with self.rwlock.r_locked():
            print("Read process")

    def write(self):
        with self.rwlock.w_locked():
            print("Write process")


if __name__ == "__main__":
    run = Example()
    t1 = threading.Thread(target=run.write)
    t2 = threading.Thread(target=run.read)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
