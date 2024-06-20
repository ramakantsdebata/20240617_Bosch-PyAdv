import threading
import time

class BankAccount:
    def __init__(self) -> None:
        self.bal = 100
        self.lock = threading.Lock()

    def deposit(self, amt):
        self.lock.acquire()
        # self.bal += amt         # Not an atomic task
        sum = self.bal
        time.sleep(1)
        sum = sum + amt
        self.bal = sum
        # Reading self.bal (100)
        ### Other thread has executed and set the actual self.bal to '50', unbeknownst to us
        # Adding the amt to the value that was read from self.bal  (100 + amt(100) = 200)
        # Assigning the sum to self.bal (self.bal = 200)
        self.lock.release()

    def withdraw(self, amt):
        with self.lock:
            self.bal -= amt

b1 = BankAccount()

t1 = threading.Thread(target=b1.deposit, args=(100,))
t2 = threading.Thread(target=b1.withdraw, args=(50,))
# b1.deposit(100)
# b1.withdraw(50)

t1.start()
t2.start()

t1.join()
t2.join()

print(b1.bal)