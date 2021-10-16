import threading


class test_thread(threading.Thread):
    def __init__(self):
        super(test_thread, self).__init__()
        threading.Thread.__init__(self)
    def run(self):
        print("这个线程在跑了")

if __name__ == '__main__':
    v = test_thread()
    v.start()
