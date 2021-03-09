from Algorithims import Algorithms
import time
import threading
import random

class BogoSort(Algorithms):
    def __init__(self, data, delay):
        Algorithms.__init__(self)

        self.data = data
        self.delay = delay

        sorting_thread = threading.Thread(target=self.sort, args=(self.data, self.drawData, self.delay))
        sorting_thread.daemon = True
        sorting_thread.start()

        self.mainloop()

    def sort(self, data, drawData, delay):
        while self.is_sorted(data) == False:
            self.shuffle(data, drawData, delay)

        drawData(self.data, ["green" for x in range(len(data))])
        time.sleep(delay)

    def shuffle(self, data, drawData, delay):
        length = len(data)
        for i in range (0, length):
            rand = random.randint(0, length - 1)
            data[i], data[rand] = data[rand], data[i]

            drawData(data, ["red" if x == i or x == rand else "white" for x in range(len(data))])
            time.sleep(delay)

    def is_sorted(self, data):
        length = len(data)
        for i in range(0, length - 1):
            if data[i] > data[i + 1]:
                return False
        return True

