import threading

class Foo:
    def __init__(self):
        self.a = threading.Event()
        self.b = threading.Event()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()

        self.a.set()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.a.wait()
        
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.b.set()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.b.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()